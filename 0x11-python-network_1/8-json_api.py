#!/usr/bin/python3

import requests
import sys

'''module: 8-json_api
accepts: single letter as command line arg
output: response from 0:0:0:0, based on input, or appropriate error msg
'''


if __name__ == '__main__':
    try:
        val = sys.argv[1]
    except:
        val = ""
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={'q': val})
    try:
        valid = len(r.json())  # this will trigger error if JSON not valid
        if valid:
            d = r.json()
            print("[{}] {}".format(d["id"], d["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
