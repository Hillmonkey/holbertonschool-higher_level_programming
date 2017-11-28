#!/usr/bin/python3

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

'''module: 2-post_email.py
accepts: 2 command line args - (1) URL, (2) email
         I think email is supposed to be a valid email address
output: body of response
'''


if __name__ == "__main__":

    url = sys.argv[1]
    data = urlencode({"email": sys.argv[2]}).encode('utf-8')
    try:
        req = Request(url, data)
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except URLError:
        pass
