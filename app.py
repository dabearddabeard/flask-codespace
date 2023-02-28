from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def arctic_frenz():
    return render_template("index.html", title="Arctic Frenz")