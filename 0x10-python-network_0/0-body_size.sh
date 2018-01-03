#!/usr/bin/env bash
# this prints Content-Size of passed inURL resource
curl -sI "$1" | grep "^Content-Length" | cut -d' ' --fields=2
