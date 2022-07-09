import os, re
from elasticsearch import Elasticsearch

def search_client():
    bonsai = os.environ['BONSAI_URL']
    auth = re.search(r'https\:\/\/(.*)\@', bonsai).group(1).split(':')
    host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

    optional_port = re.search(r'(:\d+)', host)
    if optional_port:
      p = optional_port.group(0)
      host = host.replace(p, '')
      port = int(p.split(':')[1])
    else:
      port=443

    # Connect to cluster over SSL using auth for best security:
    config = [{
     'host': host,
     'port': port,
     'use_ssl': True,
     'http_auth': (auth[0], auth[1])
    }]

    # Instantiate the new Elasticsearch connection:
    es = Elasticsearch(config)

    # Verify that Python can talk to Bonsai (optional):
    return es.ping()
