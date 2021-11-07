# This program has been developed by Mazzya
# Github: https://github.com/mazzya
# Github Project: https://github.com/Mazzya/CRUD-API-Generator

import argparse
from flask_structure import FlaskStructure
from fastapi_structure import FastApiStructure

VERSION = '1.1.0'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate CRUD APIs quickly and easily.')
    parser.add_argument('--flask', action='store_true', help='Generate a CRUD API with Flask')
    parser.add_argument('--fastapi', action='store_true', help='Generate a CRUD API with FastAPI')
    parser.add_argument('-v', '--version', action='store_true', help='Check current version')
    parser.add_argument('-p', '--path', required=False, type=str, help='Path where the API will be generated')
    args = parser.parse_args()

    if args.flask and args.path:
        flask_api = FlaskStructure()
        flask_api.generate(args.path)
    elif args.flask:
        flask_api = FlaskStructure()
        flask_api.generate()
    elif args.fastapi and args.path:
        fastapi = FastApiStructure()
        fastapi.generate(args.path)
    elif args.fastapi:
        fastapi = FastApiStructure()
        fastapi.generate()
    elif args.version:
        print(f'Current version: {VERSION}')
    else:
        print("You need to enter at least one argument, please try again.")
        parser.print_help()
