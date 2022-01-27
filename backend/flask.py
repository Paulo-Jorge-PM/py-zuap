#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, importlib

from flask import Flask
from flask_cors import CORS

from controllers import *

app = Flask(__name__, template_folder='views')
CORS(app)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

#Load de todos os controllers na pasta controllers automaticamente em vez de manual um a um
controllers = os.path.join(os.getcwd(), "controllers")
for filename in os.listdir(controllers):
    if filename.endswith(".py") and filename != "__init__.py":
        fName = filename.replace(".py","")
        package = importlib.import_module("controllers."+fName)
        module = getattr(package, fName+"Route")
        app.register_blueprint(module)

if __name__ == "__main__":
    #threaded=True
    app.run(port=8080, debug=True, host="0.0.0.0")