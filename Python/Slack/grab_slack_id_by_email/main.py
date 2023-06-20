import json
import urllib3

def get_http_manager():
    return urllib3.PoolManager()

def get_slack_user_info(user_email, token):
    slack_api_url = f"https://slack.com/api/users.lookupByEmail?email={user_email}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "authorization": f"Bearer {token}"
    }
    # response = requests.get(url=slack_api_url, headers=headers)

    http = get_http_manager()
    response = http.request("GET", slack_api_url, headers=headers)

    if response.status == 200:
        res = json.loads(response.data)

        print(json.dumps(res, indent=4))

        user_id = res.get("user", None)

        if user_id:
            return f"@{user_id['name']}"

        else:
            return "!here"


def send_slack_message_to_user(user_name):
    slack_api_url = "https://slack.com/api/chat.postMessage"
    channel = "general"
    token = "<Token-Here"
    text = f"<{user_name}> - I want you to dance like your life depended on it!"


    http = get_http_manager()
    response = http.request(
        "POST", 
        slack_api_url,
        fields={
            "token": token,
            "channel": channel,
            "text": text
        } 
    )

    if response.status == 200 and json.loads(response.data).get('ok', False):
        print("\n########################################\n")
        print(json.loads(response.data))

if __name__ == '__main__':

    user_email = "<email here>"
    token = "<token here>"

    user_name = get_slack_user_info(user_email, token)

    send_slack_message_to_user(user_name)