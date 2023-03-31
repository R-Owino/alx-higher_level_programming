#!/bin/bash
# Make request to 0.0.0.0:5000/catch_me
curl -s -X PUT -L -d "user_id=98" -H "Origin: School" "0.0.0.0:5000/catch_me" -w "\nYou got me!\n" -o /dev/null
