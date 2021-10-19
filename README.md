# CRUD-API-Generator

Check **[CHANGELOG](CHANGELOG.md)**

![GitHub release (latest by date)](https://img.shields.io/github/v/release/mazzya/CRUD-API-Generator)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?)

Generate CRUD APIs with this powerful and simple CLI program. Currently this program allows you to generate APIs with the Flask microframework. This program uses a specific file organization for API generation: 

    API Generator/
            └── app/
                ├── routes.py
                ├── app.py
                └── run.py

#### Explanation of the different files :

**app** :  This file allows you to configure the global Flask object

**routes** : This file contains all the API logic (routes, etc...)

**run** : This file allows you to run the API

### How to generate an CRUD API ?
Generating an API with this program is really easy. Let's see how to do it !
#### Requirements
```
Python 3
```
It is assumed that you already have Flask installed on your system.
#### Clone the repository
```bash
$ git clone https://github.com/Mazzya/CRUD-API-Generator-DEV.git
```
If you wish, you can download the project directly [here]()
#### Optional arguments
```
-h, --help            show this help message and exit
--flask               Generate a CRUD API with Flask
-v, --version         Check current version
-p PATH, --path PATH  Path where the API will be generated
```
In order to generate an API with Flask, it is necessary to use the `--flask` argument. If you want to generate the API in a specific directory, it is necessary to use the `-p` or `--path` argument with your directory.
#### Examples
If you wish to generate an API without specifying the directory :
```bash
$ generator.py --flask
```
If you want to generate an API in a specific directory :
```bash
$ generator.py --flask -p "C:\Users\HP\Documents"
```
The functions are already available, the only thing left for you to do is to implement the logic and eventually add a database if you need to.
#### Issues
If you find a problem with the program, feel free to [report it.](https://github.com/Mazzya/CRUD-API-Generator-DEV/issues)
#### Contribute
Any contribution is welcome ! If you wish, do not hesitate to fork the project and apply your changes there, when the changes are published create a pull request so that we can review it.
#### Important note
Currently, this program only generates APIs with [Flask](https://github.com/pallets/flask) but we are working to add support for [FastAPI](https://github.com/tiangolo/fastapi) In a future release.
