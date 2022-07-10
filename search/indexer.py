import json
import os
from client import search_client
from elasticsearch.helpers import bulk

current_directory = os.path.dirname(__file__)

def create_index():
    es = search_client()
    relative_filepath = "../data/restaurants.json"
    absolute_filepath = os.path.join(current_directory, relative_filepath)
    with open(absolute_filepath) as file:
        settings = json.load(file)
        es.indices.create(index="restaurants", body=settings)

def delete_index():
    es = search_client()
    es.indices.delete(index="restaurants")

def index_restaurants():
    es = search_client()
    locations = ["gesundbrunnen", "ostkreuz", "südkreuz", "westkreuz"]
    for location in locations:
        absolute_path = os.path.join(current_directory, f"../data/{location}.json")
        documents = []
        with open(absolute_path) as file:
            restaurants = json.load(file)
            sections = restaurants["sections"]
            items = []
            for section in sections:
                if section["name"] == "restaurants-delivering-venues":
                    items = section["items"]
            for venue in items:
                document = {"_index": "restaurants", "_id": venue["venue"]["id"], "_source": venue}
                document["_source"]["suggest"] = venue["title"]
                documents.append(document)
        bulk(es, documents)
        
if __name__ == "__main__":
    delete_index()
    create_index()
    index_restaurants()
