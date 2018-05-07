# -*- coding = utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from app.api import view

api = Blueprint("api", __name__)
api_wrap = Api(api)

api_wrap.add_resource(view.Demo, "/")
