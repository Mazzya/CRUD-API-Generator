from io import open
import argparse
import os
from flask_template import FlaskTemplate

VERSION = '1.0.0'

def generate_flask_api(path=None):
    
    flask_api = FlaskTemplate()
    
    if path:
        if os.path.exists(path):
            
            print("Generating the API...")
            
            with open(f'{path}/routes.py', 'w') as file:
                file.write(f'{flask_api.imports}\n\n{flask_api.routes}')

            with open(f'{path}/app.py', 'w') as file:
                file.write(f'{flask_api.app}')

            with open(f'{path}/run.py', 'w') as file:
                file.write(f'{flask_api.run}')
        else:
            print("Oops, there was a problem with your directory. Check if it exists and try again.")
    else:
        
        print("Generating the API in the default directory...")
        
        with open('routes.py', 'w') as file:
            file.write(f'{flask_api.imports}\n\n{flask_api.routes}')

        with open('app.py', 'w') as file:
            file.write(f'{flask_api.app}')

        with open('run.py', 'w') as file:
            file.write(f'{flask_api.run}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate CRUD APIs quickly and easily.')
    parser.add_argument('--flask', action='store_true', help='Generate a CRUD API with Flask')
    parser.add_argument('-v', '--version', action='store_true', help='Check current version')
    parser.add_argument('-p', '--path', required=False, type=str, help='Path where the API will be generated')
    args = parser.parse_args()

    if args.flask and args.path:
        generate_flask_api(args.path)
    elif args.flask:
        generate_flask_api()
    elif args.version:
        print(f'Current version: {VERSION}')
    else:
        print("Please try again")
        parser.print_help()