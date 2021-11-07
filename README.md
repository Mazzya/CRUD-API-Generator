# CRUD-API-Generator

Feel free to check the **[CHANGELOG](CHANGELOG.md)**

🎥 To see CAG in action, click [here](https://www.youtube.com/watch?v=59EZ7HwrOJc)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/mazzya/crud-api-generator)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?)

Generate CRUD APIs with this powerful and simple CLI program. Currently, this program allows to generate APIs with the following microframeworks :
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [FastAPI](https://fastapi.tiangolo.com/) 

This program uses a specific file organization for API generation when using Flask : 

    MyAPI/
            └── app/
                ├── routes.py
                ├── app.py
                └── run.py

#### Explanation of the different files for API generation with Flask :

`app` :  This file allows you to configure the global Flask object

`routes` : This file contains all the API logic (routes, etc...)

`run` : This file allows you to run the API

### How to generate an CRUD API ?
Generating an API with this program is really easy. Let's see how to do it !

#### Requirements
```
Python 3
```
It is assumed that you have already installed the framework for which you are going to generate the API.
#### Clone the repository
```bash
$ git clone https://github.com/Mazzya/CRUD-API-Generator-DEV.git
```
If you wish, you can download the project directly [here](https://github.com/Mazzya/CRUD-API-Generator/releases)
#### Optional arguments
```
-h, --help            show this help message and exit
--flask               Generate a CRUD API with Flask
--fastapi             Generate a CRUD API with FastAPI
-v, --version         Check current version
-p PATH, --path PATH  Path where the API will be generated
```
### Examples
Let's see how to generate an API with Flask and FastAPI.
#### Generate an API with Flask
If you wish to generate an API without specifying the directory :
```bash
$ generator.py --flask
```
If you want to generate an API in a specific directory :
```bash
$ generator.py --flask -p "C:\Users\HP\Documents"
```
#### Generate an API with FastAPI
If you wish to generate an API without specifying the directory :
```bash
$ generator.py --fastapi
```
If you want to generate an API in a specific directory :
```bash
$ generator.py --fastapi -p "C:\Users\HP\Documents"
```
The functions are already available, the only thing left for you to do is to implement the logic and eventually add a database if you need to.
#### Issues
If you find a problem with the program, feel free to [report it.](https://github.com/Mazzya/CRUD-API-Generator/issues)
#### Contribute
Any contribution is welcome ! If you wish, do not hesitate to fork the project and apply your changes there, when the changes are published create a pull request so that we can review it.
#### Important note
Currently, this program only generates APIs with [Flask](https://github.com/pallets/flask) and [FastAPI](https://github.com/tiangolo/fastapi). It is possible that more frameworks will be added in the next versions.
#### Discord Server
We have a discord server in case you have any questions or want to be informed about the project news. Do not hesitate to [join us](https://discord.gg/mZF9ywQzdg), we are waiting for you.
