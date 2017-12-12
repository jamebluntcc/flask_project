# coding=utf-8
from flask import render_template, Blueprint

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    return render_template('index.html')
