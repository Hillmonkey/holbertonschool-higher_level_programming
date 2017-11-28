#!/usr/bin/python3

import requests
import sys

'''module: 9-starwars
accepts: string as command line arg
queries swapi, searching for 'string' in people database of SWAPI
output: number of star wars characters matching the api, and list a list
        of those characters
ex: https://swapi.co/api/people/?search=r2
'''


if __name__ == '__main__':
    url = "https://swapi.co/api/people/"
    payload = {"search": sys.argv[1]}
    r = requests.get(url, params=payload)
    d = r.json()
    print("Number of results: {}".format(d["count"]))
    for person in d["results"]:
        print(person["name"])
