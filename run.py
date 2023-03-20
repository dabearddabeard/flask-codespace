"""" run.py """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/spy')
def about():
    return render_template('spy.html')



app.debug = "development"
app.run(debug=True)
