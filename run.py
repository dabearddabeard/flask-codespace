"""This module sets the Flask app environment to development and runs the app in debug mode."""

from my_app import app
app.debug = "development"
app.run(debug=True)
