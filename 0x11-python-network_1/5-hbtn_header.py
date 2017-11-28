#!/usr/bin/python3

import requests
import sys

'''module: 5-hbtn_header
accepts: URL from the command line
output: value of X-Request-Id
'''


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
