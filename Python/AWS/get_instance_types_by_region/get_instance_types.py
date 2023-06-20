import json
import os
import uuid
import boto3

def create_client(region):
    return boto3.client('ec2', region_name=region)


def specific_instance_types(region, instance_types):
    client = create_client(region)
    output = []
    for inst in instance_types:
        print(inst)
        response = client.describe_instance_types(
            InstanceTypes = [inst]
        )

        print(json.dumps(response, indent=4))

        it = response['InstanceTypes'][0]

        print(it)

        it_info = {
            "instance_type": it['InstanceType'],
            "current_generation": it.get('CurrentGeneration', None),
            "free_tier_eligible": it.get('FreeTierEligible', None),
            "usages": it.get('SupportedUsageClasses', None),
            "vcpu_info": it.get('VCpuInfo', None),
            "memory": it.get('MemoryInfo', None),
            "instance_storage_supported": it.get('InstanceStorageSupported', None),
            "instance_storage_info": it.get('InstanceStorageInfo', None),
            "ebs_info": it.get('EbsInfo', None)
        }

        print(json.dumps(it_info, indent=4))

        output.append(it_info)

    print("Writing file...")
    filename = f"specific_instances_{region}.json"
    json_object = json.dumps(output, indent=4)
    with open(filename, 'w') as outfile:
        outfile.write(json_object)

    outfile.close()
    print("File Closed")


def get_allowed_instance_types(region):
    count = 0
    output = []
    client = create_client(region)

    response = client.describe_instance_types()

    next_token = response.get('NextToken', None)

    # print(json.dumps(response['InstanceTypes'], indent=4))

    for it in response['InstanceTypes']:
        it_info = {
            "instance_type": it['InstanceType'],
            "current_generation": it.get('CurrentGeneration', None),
            "free_tier_eligible": it.get('FreeTierEligible', None),
            "usages": it.get('SupportedUsageClasses', None),
            "vcpu_info": it.get('VCpuInfo', None),
            "memory": it.get('MemoryInfo', None),
            "instance_storage_supported": it.get('InstanceStorageSupported', None),
            "instance_storage_info": it.get('InstanceStorageInfo', None),
            "ebs_info": it.get('EbsInfo', None)
        }

        output.append(it_info)

    while next_token != None:
        count += 1
        print(count)
        print(next_token)
        additional_response = client.describe_instance_types(NextToken=next_token)
        next_token = additional_response.get('NextToken', None)
        for it in additional_response['InstanceTypes']:
            it_info = {
                "instance_type": it['InstanceType'],
                "current_generation": it.get('CurrentGeneration', None),
                "free_tier_eligible": it.get('FreeTierEligible', None),
                "usages": it.get('SupportedUsageClasses', None),
                "vcpu_info": it.get('VCpuInfo', None),
                "memory": it.get('MemoryInfo', None),
                "instance_storage_supported": it.get('InstanceStorageSupported', None),
                "instance_storage_info": it.get('InstanceStorageInfo', None),
                "ebs_info": it.get('EbsInfo', None)
            }

            output.append(it_info)

    print("Writing file...")
    filename = f"{region}.json"
    json_object = json.dumps(output, indent=4)
    with open(filename, 'w') as outfile:
        outfile.write(json_object)

    outfile.close()
    print("File Closed")


def main():
    closing_responses = ['q', 'quit', 'exit', 'x', 'close', 'done']

    user_response = input("Please enter the region you wish to collect available instance types on: ")
    try:
        while user_response.lower() not in closing_responses:
            print("Starting job...")
            get_allowed_instance_types(user_response)

            specific_instance_types(
                user_response,
                [
                    'm5ad.xlarge',
                    'm5d.xlarge',
                    'm5ad.2xlarge',
                    'm5d.2xlarge',
                    't3.2xlarge',
                    'm5d.4xlarge',
                    'm6i.4xlarge',
                    'c5.large',
                    'c5ad.large',
                    'c5d.large',
                    'c6i.large',
                    't3.medium'
                ]
            )
            print("Job Complete!")

            user_response = input("Please enter the region you wish to collect available instance types on: ")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()