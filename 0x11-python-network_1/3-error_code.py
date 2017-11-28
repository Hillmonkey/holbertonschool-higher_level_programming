#!/usr/bin/python3

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import urllib.error

'''module: 3-error-code
accepts: name of url as command line arg
output: body of response
'''


if __name__ == "__main__":

    url = sys.argv[1]
    try:
        req = Request(url)
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
