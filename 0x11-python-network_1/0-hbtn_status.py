#!/usr/bin/python3
from urllib import request
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
	req = request
	
	with req.urlopen("https://alx-intranet.hbtn.io/status") as resp:
	    data = resp.read()
	
	print("Body response:")
	print(f"    - type: {type(data)}")
	print(f"    - content: {data}")
	print("    - utf8 content: {}".format(data.decode("utf-8")))
