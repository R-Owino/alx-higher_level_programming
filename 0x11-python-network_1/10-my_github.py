#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    api = 'https://api.github.com/user'

    response = requests.get(api, auth=auth)

    print(response.json().get('id'))
