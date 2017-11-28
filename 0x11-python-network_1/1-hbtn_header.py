#!/usr/bin/python3

import sys
from urllib.request import Request, urlopen, urlretrieve

'''module: 1-hbtn_header.py
accepts: URL from the command line
output: value of X-Request-Id
'''


if __name__ == "__main__":

    try:
        req = Request(sys.argv[1])
        with urlopen(req) as response:
            print(response.getheader('X-Request-Id'))
    except URLError:
        pass
