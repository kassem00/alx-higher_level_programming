#!/usr/bin/python3
"""
Python script that takes in a URL,
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
