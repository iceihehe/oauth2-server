# -*- coding = utf-8 -*-

import logging

from flask import Flask

from app.config import Config


def create_app():

    app = Flask(Config.PROJECT_NAME, template_folder="dist", static_folder="dist")

    config_logging()
    config_blueprint(app)

    return app


def config_logging():

    logging.basicConfig(level=logging.INFO)


def config_blueprint(application):
    """

    :type application: Flask
    """

    from app.api import api
    application.register_blueprint(api)

