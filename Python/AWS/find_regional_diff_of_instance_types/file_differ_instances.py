import json

def find_the_rogues(file_one, file_two):
    data_one = {}
    data_two = {}

    output = {}

    with open(file_one) as f1:
        data_one = json.load(f1)

    with open(file_two) as f2:
        data_two = json.load(f2)


    for i in data_one:
        for j in data_two:
            if i['instance_type'] == j['instance_type']:
                output.update({i['instance_type']: {"Regions": "Both"}})
                continue

        if i['instance_type'] not in output:
            output.update({i['instance_type']: {"Regions": file_one.split('.')[0]}})
            continue

    for k in data_two:
        for l in data_one:
            if k['instance_type'] == l['instance_type']:
                output.update({k['instance_type']: {"Regions": "Both"}})
                continue

        if k['instance_type'] not in output:
            output.update({k['instance_type']: {"Regions": file_two.split('.')[0]}})
            continue

    return output


def main():
    closing_responses = ['q', 'quit', 'exit', 'x', 'close', 'done']

    first_response = input("Enter the first file: ")
    second_response = input("Enter the second file: ")

    while first_response not in closing_responses or second_response not in closing_responses:
        response = find_the_rogues(first_response, second_response)

        filename = f"diff_{first_response.split('.')[0]}_{second_response.split('.')[0]}.json"

        with open(filename, 'w') as f:
            f.write(json.dumps(response, indent=4, sort_keys=True))

        f.close()

        first_response = input("Enter the first file: ")
        second_response = input("Enter the second file: ")


if __name__ == "__main__":
    main()
