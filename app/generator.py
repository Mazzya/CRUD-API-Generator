from io import open
import argparse
import os
from flask_structure import *
VERSION = '1.0.0'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate CRUD APIs quickly and easily.')
    parser.add_argument('--flask', action='store_true', help='Generate a CRUD API with Flask')
    parser.add_argument('-v', '--version', action='store_true', help='Check current version')
    parser.add_argument('-p', '--path', required=False, type=str, help='Path where the API will be generated')
    args = parser.parse_args()

    if args.flask and args.path:
        flaskTemplate = FlaskStructure()
        flaskTemplate.generate(args.path)
    elif args.flask:
        flaskTemplate = FlaskStructure()
        flaskTemplate.generate()
    elif args.version:
        print(f'Current version: {VERSION}')
    else:
        print("Please try again")
        parser.print_help()