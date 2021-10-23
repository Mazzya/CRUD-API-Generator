#!/usr/bin/python
# This program has been developed by Mazzya
# Github: https://github.com/mazzya
# Github Project: https://github.com/Mazzya/CRUD-API-Generator

import os

class FlaskTemplate:    
    app = 'from flask import Flask\n\napp = Flask(__name__)'
    
    run = """import app\n\nif __name__ == '__main__': 
    app.run()"""
    
    routes = """from flask import Flask, jsonify\nfrom app import app\n\n# Home page
@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to this simple Flask API generated by CAG',
        'author': 'Mazzya',
        'Github': 'https://www.github.com/Mazzya',
        'Github Project': 'https://github.com/Mazzya/crud-api-generator'
    })

# Add new product
@app.route('/products', methods = ['POST'])
def addProduct():
    pass

# Get all products
@app.route('/products')
def getProducts():
    pass

# Update product
@app.route('/products/<int:id>', methods=['PUT'])
def editProduct(id):
    pass

# Delete product
@app.route('/products/<int:id>', methods = ['DELETE'])
def deleteProduct(id):
    pass

# This function handles 404 error
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'page not found !'})"""


class FlaskStructure:

    def __init__(self):
        self.flask_api = FlaskTemplate()
        self.content = {
            'run':self.flask_api.run,
            'app':self.flask_api.app,
            'routes':self.flask_api.routes
        }
        
    def generate(self,path = None):

        if not path or not os.path.exists(path):
            print("Generating the API in the default directory...")
        else:
            print(f"Generating the API in a specific directory: {path}")
        
        for key in self.content:
            route  = "{pathName}/{fileName}.py".format(pathName=path,fileName=key) if path else "{fileName}.py".format(fileName=key)
            try:
                with open(f'{route}', 'w') as file:
                    file.write(f'{self.content[key]}')
            except FileNotFoundError:
                print("Oops, there was a problem with the file generation. Please check if the directory exists and try again.")
                break
    





    
