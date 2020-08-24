#!/usr/bin/python3
"""status python network"""
import requests
import sys


if __name__ == '__main__':

    user = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/users/{}'.format(user)

    headers = {'Authorization': 'token ' + password, 'Accept': 'application/vnd.github.v3+json'}
    result = requests.get(url, headers=headers)

    try:
        result.raise_for_status()
        print(result.json().get("id"))

    except requests.exceptions.RequestException as e:
        print("None")
