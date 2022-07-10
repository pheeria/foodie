def to_frontend(es_response):
    result = []

    if es_response and 'hits' in es_response:
        for each in es_response['hits'].get('hits', []):
            restaurant = each['_source']
            document = {
                'image': restaurant['image']['url'],
                'url': f'https://wolt.com/en/deu/berlin/restaurant/{restaurant["venue"]["slug"]}',
                'title': restaurant['title'],
                'subtitle': restaurant['venue']['short_description'],
                'rating': '😅'
            }

            if 'rating' in restaurant['venue']:
                if restaurant['venue']['rating']['score'] >= 9.0:
                    document['rating'] = '😁'
                elif restaurant['venue']['rating']['score'] >= 7.0:
                    document['rating'] = '🙂'
                else:
                    document['rating'] = '😐'

            result.append(document)

    return result
