#!/usr/bin/python3

import requests
import sys

'''module: 10-my_github
accepts: string as command line arg
queries swapi, searching for 'string' in people database of SWAPI
output: number of star wars characters matching the api, and list a list
        of those characters
ex: https://swapi.co/api/people/?search=r2
'''


if __name__ == '__main__':
    url = "https://api.github.com/users/"
    user = sys.argv[1]
    passwd = sys.argv[2]
    r = requests.get(url, auth=(user, passwd))
    d = r.json()
    print(d.get('id'))
