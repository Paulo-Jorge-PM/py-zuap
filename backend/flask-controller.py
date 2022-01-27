#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify
from models import db, queries

contactRoute = Blueprint('flask-controller', __name__,  template_folder='views')

@contactRoute.route('/flask-controller')
def flaskController():
    if request.method == "GET":
        return render_template("flask-controller.html", title="Controller")
        #Dict to json:
        #return jsonify(results)
    elif request.method == "POST":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    