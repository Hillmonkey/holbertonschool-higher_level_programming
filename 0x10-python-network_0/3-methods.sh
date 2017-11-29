#!/bin/bash
# this accepts URL and prints body of HTTP response
curl -sI "$1" -X OPTIONS | grep ^Allow: | cut -d' ' -f2-10
