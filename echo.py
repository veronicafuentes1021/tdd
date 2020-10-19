#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Veronica Fuentes"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Process input text.")
    parser.add_argument(
        '-u', '--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument(
        '-l', '--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument(
        '-t', '--title', action='store_true', help='convert text to titlecase')
    parser.add_argument(
        'txt', help='words input')
    if not sys.argv:
        parser.print_usage()
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args()
    if args.upper:
        print(args.txt.upper())
    elif args.lower:
        print(args.txt.lower())
    elif args.title:
        print(args.txt.title())
    else:
        print(args.txt)


if __name__ == '__main__':
    main(sys.argv[1:])
