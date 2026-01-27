#!/usr/bin/env python3
"""
Docstring for python_setup
"""

import requests


def main():
    """
    Docstring for main
    """
    url = "http://wttr.in/Tulcea"
    response = requests.get(url, timeout=15)
    print("Weather info:", response.text)


if __name__ == "__main__":
    main()
