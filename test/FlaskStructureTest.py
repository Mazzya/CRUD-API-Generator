
# Bring your packages into the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'app')))

from flask_structure import *


flaskTemplate = FlaskStructure()

flaskTemplate.generate()

