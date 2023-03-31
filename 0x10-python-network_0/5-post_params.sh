#!/bin/bash
#  script that takes in a URL as an argument, sends a POST request to the URL
curl -sSL -d "email=test@gmail.com&subject=I'll always be here for PLD" "$1"
