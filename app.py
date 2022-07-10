from flask import Flask, request, render_template
from search.client import search_client
from search.transformations import to_frontend

app = Flask(__name__)

@app.route("/autocomplete")
def autocomplete():
    es = search_client()
    query = request.args.get('q', '')
    response = es.search(index='restaurants', body={
        'query': {
            'match': {
                'venue.name': query
            }
        }
    })

    results = to_frontend(response)
    return render_template('index.html', results=results)

@app.route("/")
def index():
    es = search_client()
    query = request.args.get('q', '')
    response = es.search(index='restaurants', body={
        'query': {
            'match': {
                'venue.name': query
            }
        }
    })

    results = to_frontend(response)
    return render_template('index.html', results=results)
