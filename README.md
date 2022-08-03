# Foodie

## Setup

1. Install dependencies
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Setup elastic search
```sh
bash run_elastic.sh
```
and in the separate terminal
```sh
python search/indexer.py
```

3. Local development
```sh
export FLASK_ENV=development
flask run --port 4200
```


## FAQ

> Where did you get the data from?

From Wolt website, using four locations of Berlin.
This resulted in 2048 unique restaurants.

```sh
curl 'https://restaurant-api.wolt.com/v1/pages/restaurants?lat=52.5024674&lon=13.2810506' \
    -H 'Accept: application/json' > ./data/westkreuz.json

curl 'https://restaurant-api.wolt.com/v1/pages/restaurants?lat=52.4757114&lon=13.3632231' \
    -H 'Accept: application/json' > ./data/südkreuz.json

curl 'https://restaurant-api.wolt.com/v1/pages/restaurants?lat=52.5031692&lon=13.4671454' \
    -H 'Accept: application/json' > ./data/ostkreuz.json

curl 'https://restaurant-api.wolt.com/v1/pages/restaurants?lat=52.5487585&lon=13.3844482' \
    -H 'Accept: application/json' > ./data/gesundbrunnen.json
```

> Is this production-ready?

No 😅
It's missing:
- defensive programming against network calls
- asynchoronous calls
- logging/tracing
- tests (load tests, e2e tests, stress tests, unit tests)

> Why are there no tests?

Initially there used to be `pytest` included into requirements, however because of the small scope, there is not much logic to test, apart from the json transformations.

> Why are there no formatters and/or linters?

I have Pyright installed locally and my OCD doesn't let me write misaligned code. That's definitely a need for a project with multiple people involved.

> Is there anything missing in the UI?

Keyboard navigation for the Autocomplete and some accessibility improvements.

> What can be done better for Search?

- Filtering with facets
- Availability awareness
- Location/deliverability awareness
- Synonyms
- Expansions and classifications

> Is there any tracking?

Take a look into the Dev Tools console!
