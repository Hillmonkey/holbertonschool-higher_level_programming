#!/usr/bin/python3

from urllib.request import Request, urlopen

'''module: 0-hbtn_status
output: various info from HTTP response
'''


if __name__ == "__main__":

    req = Request('https://intranet.hbtn.io/status')
    # response = urlopen(reg)
    with urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode("utf-8")))
