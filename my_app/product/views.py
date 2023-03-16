"""
This module defines routes for a Flask application using the Blueprint object.

The `product_blueprint` object is an instance of the `Blueprint` class from the Flask framework. It is used to define routes for a product-related section of a Flask application.

The `home` function defines two routes: `/` and `/home`. Both routes render and return the `home.html` template with a context variable `products`, which contains all products from the `PRODUCTS` dictionary imported from `my_app.product.models`.

The `product` function defines a route with a dynamic URL: `/product/<key>`. The route renders and returns the `product.html` template with a context variable `product`, which contains information about a specific product identified by its key. If no product is found with the given key, an HTTP 404 error is raised using the Flask's abort function.
"""

from flask import abort
from flask import render_template
from flask import Blueprint
from my_app.product.models import PRODUCTS

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)