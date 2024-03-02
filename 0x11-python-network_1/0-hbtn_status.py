#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    with urllib.request.urlopen(url) as response:
        data = response.read()
        
    print("Body response:")
    print(f"    - type: {type(data)}")
    print(f"    - content: {data}")
    print("    - utf8 content: {}".format(data.decode("utf-8")))
