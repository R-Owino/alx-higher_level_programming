#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response
using requests package
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
