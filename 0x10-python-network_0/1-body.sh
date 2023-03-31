#!/bin/bash
# script that takes in a URL, sends a GET request to the URL using curl, and displays the body of the response if the response status code is 200
curl -sSLw "%{http_code}" "$1" | grep -q 200 && curl -sSL "$1"
