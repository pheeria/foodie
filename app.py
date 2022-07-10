from flask import Flask, render_template, request, jsonify

from search.client import search_client
from search.transformations import to_frontend_results, to_frontend_suggestions

app = Flask(__name__)

@app.route("/autocomplete")
def autocomplete():
    es = search_client()
    query = request.args.get("q", "")
    response = es.search(index="restaurants", body={
        "suggest": {
            "autocomplete": {
                "prefix": query,
                "completion": {
                    "field": "suggest",
                    "skip_duplicates": True,
                }
            }
        },
        "_source": "title"
    })

    return jsonify(to_frontend_suggestions(response))


@app.route("/")
def index():
    es = search_client()
    query = request.args.get("q", "")
    response = es.search(index="restaurants", body={
        "query": {
            "match": {
                "venue.name": query
            }
        }
    })

    results = to_frontend_results(response)
    return render_template("index.html", results=results)
