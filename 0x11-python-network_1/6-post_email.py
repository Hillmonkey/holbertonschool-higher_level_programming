#!/usr/bin/python3

import requests
import sys

'''module: 6-post_email
accepts: 2 command line args (1) URL, (2) email
output: body of response
'''


if __name__ == '__main__':
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
