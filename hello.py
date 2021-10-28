from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/character/<name>")
def heuj(name):
    return render_template('testtemplate.html', a_variable=name)
    # return f'<p>Vlinderstrikjes</p> {escape(name)}'