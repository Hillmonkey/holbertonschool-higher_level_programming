#!/usr/bin/python3

import requests
import sys

'''module: 7-error_code
accepts: URL from command line
output: body of response or error code if status code >= 400
'''


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
