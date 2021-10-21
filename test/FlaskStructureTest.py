
# Bring your packages into the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'app')))

from flask_structure import *

if __name__ == '__main__':
    flaskTemplate = FlaskStructure()
    flaskTemplate.generate()

