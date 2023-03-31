#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and displays the response body
curl -sSLX DELETE "$1"
