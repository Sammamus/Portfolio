import json
import os
import uuid
import boto3

def create_client(region):
    return boto3.client('ec2', region_name=region)

def get_availability_zones(region):
    client = create_client(region)

    output = []

    response = client.describe_availability_zones(
        Filters=[
            {
                'Name': 'region-name',
                'Values': [region]
            }
        ]
    )

    for az in response['AvailabilityZones']:
        output.append(az['ZoneName'])

    # print(json.dumps(response, indent=4))

    return output


def collect_data_offerings(region, instance_type, location_type, avail_zone=None):
    count = 0
    output = []
    client = create_client(region)

    location_value = region if location_type == 'region' else avail_zone

    response = client.describe_instance_type_offerings(
        LocationType=location_type,
        Filters=[
            {
                'Name': 'location',
                'Values': [location_value]
            },
            {
                'Name': 'instance-type',
                'Values': [instance_type]
            }
        ]
    )

    next_token = response.get('NextToken', None)

    for it in response['InstanceTypeOfferings']:
        it_info = {
            "instance_type": it['InstanceType'],
            "location_type": it.get('LocationType', None),
            "location": it.get('Location', None),
            "status": "OFFERED"
        }

        output.append(it_info)

    while next_token != None:
        count += 1
        print(count)
        print(next_token)
        additional_response = client.describe_instance_types(
            LocationType=location_type,
            Filters=[
                {
                    'Name': 'location',
                    'Values': [location_value]
                },
                {
                    'Name': 'instance-type',
                    'Values': [instance_type]
                }
            ]
        )
        next_token = additional_response.get('NextToken', None)
        for it in additional_response['InstanceTypeOfferings']:
            it_info = {
                "instance_type": it['InstanceType'],
                "location_type": it.get('LocationType', None),
                "location": it.get('Location', None),
                "status": "OFFERED"
            }

            output.append(it_info)

    return output

def get_instance_offerings(region, instance_type):
    packaged_output = {
        "Region": region,
        "Instance-Type": instance_type
    }
    output = []

    availability_zones = get_availability_zones(region)
    packaged_output['Availability-Zones'] = availability_zones

    region_response = collect_data_offerings(region, instance_type, 'region')
    print(json.dumps(region_response, indent=4))

    if region_response != []:
        output += region_response

    else:
        output += [
            {
                "instance_type": instance_type,
                "location_type": "region",
                "location": region,
                "status": "NOT OFFERED"
            }
        ]

    for av_zone in availability_zones:
        az_response = collect_data_offerings(region, instance_type, 'availability-zone', av_zone)
        print(json.dumps(az_response, indent=4))

        if az_response != []:
            output += az_response

        else:
            output += [
                {
                    "instance_type": instance_type,
                    "location_type": "availability-zone",
                    "location": av_zone,
                    "status": "NOT OFFERED"
                }
            ]


    packaged_output['Offerings'] = output

    print("Writing file...")
    filename = f"{region}-{instance_type}-offerings.json"
    json_object = json.dumps(packaged_output, indent=4)
    with open(filename, 'w') as outfile:
        outfile.write(json_object)

    outfile.close()
    print("File Closed")


def main():
    closing_responses = ['q', 'quit', 'exit', 'x', 'close', 'done']

    region = input("Please enter the AWS region you wish to collect data on: ")
    instance_type = input("Please enter the instance you wish to look for:  ")
    try:
        while region.lower() not in closing_responses:
            print("Starting job...")
            get_instance_offerings(region, instance_type)

            print("Job Complete!")

            region = input("Please enter the AWS region you wish to collect data on: ")
            instance_type = input("Please enter the instance you wish to look for:  ")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()