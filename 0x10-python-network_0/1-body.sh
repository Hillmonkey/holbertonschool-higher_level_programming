#!/usr/bin/env bash
# this accepts URL and prints body of HTTP response
STATUSCODE=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$STATUSCODE" = 200 ]; then
    curl -s "$1"
fi
