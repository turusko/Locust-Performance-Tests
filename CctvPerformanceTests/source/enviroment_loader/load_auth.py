import json


def get_auth_token():
    with open("auth.json", "r") as open_file:
        auth_json = json.load(open_file)
    return auth_json["accessToken"]
