#!/usr/bin/python3
"""status python network"""
import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    user = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'.format(user, repo)
    headers = {'Accept': 'application/vnd.github.v3+json'}
    result = requests.get(url, headers=headers)

    try:
        result.raise_for_status()
        res_json = result.json()
        for el in res_json:

            author_name = el.get("commit").get("author").get("name")
            author_commit_sha = el.get("sha")
            print("{}: {}".format(author_commit_sha, author_name))
    except requests.exceptions.RequestException as e:
        print("None")
