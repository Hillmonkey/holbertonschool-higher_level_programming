#!/usr/bin/python3

import requests

'''module: 4-hbtn_status
fetches: hardcoded website
returns: body, and info
'''


if __name__ == '__main__':
    r = requests.get("https://intranet.hbtn.io/status")
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
