#!/bin/bash
# this accepts URL and sends delete request
curl -s "$1" -X DELETE
