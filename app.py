from flask import Flask, request, render_template
from search.client import search_client

app = Flask(__name__)

@app.route("/")
def hello_world():
    es = search_client()
    query = request.args.get('q', '')
    response = es.search(index='restaurants', body={
        'query': {
            'match': {
                'venue.name': query
            }
        }
    })
    results = map(lambda each: each['_source'], response['hits']['hits'])
    return render_template('index.html', results=list(results))
