#!/usr/bin/python3
"""
Python script that takes in a URL,
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    reqs = request.Request(sys.argv[1], data)
    with request.urlopen(reqs) as response:
        print(response.read().decode("utf-8"))
