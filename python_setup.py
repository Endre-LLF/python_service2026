#!/usr/bin/env python3
"""
Docstring for python_setup
"""

import requests


def main():
    """
    Docstring for main
    """
    url = "https://wttr.in/Tulcea?format=3"
    response = requests.get(url, timeout=5)
    print("Weather info:", response.text)


if __name__ == "__main__":
    main()
