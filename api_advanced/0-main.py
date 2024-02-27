#!/usr/bin/python3
"""
0-main
A script to print the number of subscribers for a given subreddit.

Usage:
  ./0-main.py <subreddit_name>

Example:
  ./0-main.py python
"""

import sys

if __name__ == '__main__':
    """
    Main entry point of the script.
    
    If a subreddit name is provided as a command-line argument,
    it prints the number of subscribers for that subreddit.
    """
    
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))