#!/usr/bin/python3

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

'''module: 3-error-code
accepts: name of url as command line arg
output: body of response
'''


if __name__ == "__main__":

    url = sys.argv[1]
    try:
        req = Request(url)
        with urlopen(req) as response:
            response.read().decode('utf-8')
    except URLError:
        pass
