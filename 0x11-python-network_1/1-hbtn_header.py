#!/usr/bin/python3
"""
Python script that takes in a URL,
"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)

    with request.urlopen(req) as resp:
        request_id = resp.getheader('X-Request-Id')
        if request_id:
            print(request_id)
