#!/usr/bin/python
# This program has been developed by Mazzya
# Github: https://github.com/mazzya
# Github Project: https://github.com/Mazzya/CRUD-API-Generator

import os


class FastApiTemplate:
    app = """from fastapi import FastAPI\n\napp = FastAPI(
    title='API',
    description='A simple API generated with CAG (CRUD-API-Generator)',
    version='0.0.1')"""

    routes = """from app import app\n\n\n# Home page
@app.get('/')
async def home():
    return {
        'message': 'Welcome to this simple API generated with CAG and FastAPI',
        'author': 'Mazzya',
        'Github': 'https://www.github.com/Mazzya',
        'Github Project': 'https://github.com/Mazzya/crud-api-generator'
    }


# Add new product
@app.post('/products')
async def add_product():
    pass


# Get all products
@app.get('/products')
async def get_products():
    pass


# Get product per ID
@app.get('/products/{product_id}')
async def get_product(product_id: str):
    pass


# Update product
@app.put('/products/{product_id}')
async def update_product(product_id: str):
    pass


# Delete product
@app.delete('/products/{product_id}')
async def delete_product(product_id: str):
    pass
"""


class FastApiStructure:

    def __init__(self):
        self.fastapi = FastApiTemplate()
        self.content = {
            'app': self.fastapi.app,
            'routes': self.fastapi.routes
        }

    def generate(self, path=None):
        if not path or not os.path.exists(path):
            print("Generating the API in the default directory...")
        else:
            print(f"Generating the API in a specific directory: {path}")

        for key in self.content:
            route = "{pathName}/{fileName}.py".format(pathName=path, fileName=key) if path else "{fileName}.py".format(fileName=key)
            try:
                with open(f'{route}', 'w') as file:
                    file.write(f'{self.content[key]}')
            except FileNotFoundError:
                print("Oops, there was a problem with the file generation. Please check if the directory exists and "
                      "try again.")
                break
