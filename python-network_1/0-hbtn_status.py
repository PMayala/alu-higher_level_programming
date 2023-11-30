#!/usr/bin/python3
"""
A script that fetches different URLs using urllib.
"""

import urllib.request

def fetch_url(url):
    """
    Fetches a URL and prints relevant information.
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")

if __name__ == '__main__':
    # Fetching https://intranet.hbtn.io/status
    fetch_url('https://intranet.hbtn.io/status')

    # Fetching http://0.0.0.0:5050/status instead of https://intranet.hbtn.io/status
    fetch_url('http://0.0.0.0:5050/status')
