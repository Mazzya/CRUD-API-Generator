#!/usr/bin/python
import os
from flask_template import FlaskTemplate

class FlaskStructure:

    def __init__(self):
        self.flask_api = FlaskTemplate()
        self.content = {
            "run":self.flask_api.run,
            "app":self.flask_api.app,
            "routes":self.flask_api.routes
        }
        
    def generate(self,path = None):

        if not path or not os.path.exists(path):
            print("Generating the API in the default directory...")
        else:
            print("Generating the API in a specific directory: %s" % path)
        
        for key in self.content:
            route  = "{pathName}/{fileName}.py".format(pathName=path,fileName=key) if path else "{fileName}.py".format(fileName=key)
            try:
                with open(f'{route}', 'w') as file:
                    file.write(f'{self.content[key]}')
            except:
                print("An error ocurred:  writting content in filename %s.py" % filename)





    
