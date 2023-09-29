#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    r = get('https://api.github.com/Caesar254', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
