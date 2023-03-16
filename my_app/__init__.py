"""This module creates and configures a Flask app."""

from flask import Flask
from my_app.product.views import product_blueprint

app = Flask(__name__, static_url_path='/my_app/static', static_folder='/static')
app.register_blueprint(product_blueprint)
