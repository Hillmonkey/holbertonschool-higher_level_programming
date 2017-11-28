#!/usr/bin/env bash
# this prints Content-Size of URL resource
# curl -I $1 | grep Content-Size
curl -sI 0.0.0.0:5000 | grep "^Content-Length" | cut -d' ' --fields=2
