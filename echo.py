#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Mike Boring"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    parser.add_argument('text', type=str, help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action="store_true")
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action="store_true")
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action="store_true")

    ns = parser.parse_args(args)
    new_string = ''
    if not ns:
        parser.print_usage()
        sys.exit(1)
    string = args[0]
    if len(args) == 1:
        new_string = string
    if len(args) > 2:
        new_string = string
        for x in args:
            if x == '-u' or x == '--upper':
                new_string = new_string.upper()
                continue
            if x == '-l' or x == '--lower':
                new_string = new_string.lower()
                continue
            if x == '-t' or x == '--title':
                new_string = new_string.title()
                continue
    else:
        if ns.lower:
            new_string = string.lower()
        if ns.upper:
            new_string = string.upper()
        if ns.title:
            new_string = string.title()
        if ns.title == False and ns.upper == False and ns.lower == False:
            new_string = string

    print(new_string)


if __name__ == '__main__':
    main(sys.argv[1:])
