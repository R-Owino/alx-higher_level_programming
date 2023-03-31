#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL with the "X-School-User-Id" header set to 98, and displays the body of the response
curl -sSLH "X-School-User-Id: 98" "$1"
