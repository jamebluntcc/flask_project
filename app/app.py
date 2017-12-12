from flask import Flask, render_template
from settings import config
from . import main
from .extensions import bcrypt


def create_app(config_name='prod'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_handlerrors(app)

    return app


def register_extensions(app):
    bcrypt.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(main.views.blueprint)
    return None


def register_handlerrors(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
