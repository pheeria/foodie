import os, re
from elasticsearch import Elasticsearch

def search_client() -> Elasticsearch:
    host = "https://bonsai.io"
    port = 443
    auth = ("admin", "password")

    bonsai = os.environ["BONSAI_URL"]
    # url is in https://<user>:<password>@<host>:<port> format
    url = re.search(r"https://(.*):(.*)\@(.*):(\d+)", bonsai)
    if url:
        auth = (url.group(1), url.group(2))
        host = url.group(3)
        port = url.group(4)

    config = [{
     "host": host,
     "port": port,
     "use_ssl": True,
     "http_auth": (auth[0], auth[1])
    }]

    return Elasticsearch(config)
