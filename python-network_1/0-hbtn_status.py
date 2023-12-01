#!/usr/bin/python3
"""
A script that fetches https://alu-intranet.hbtn.io/status using urllib.
"""

import urllib.request

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content))

# Date: 2023-12-01 00:10:37 -0800
# README.md exists and is not empty
# File is present
# Correct output for fetching https://intranet.hbtn.io/status
# Correct output for fetching http://0.0.0.0:5050/status instead of https://intranet.hbtn.io/status
# PEP8 validation
