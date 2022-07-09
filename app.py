from flask import Flask, render_template
from search import search_client

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', a_variable=search_client())
