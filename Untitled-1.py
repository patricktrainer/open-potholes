#%%
from requests import get


def service_calls(url, payload):
    response = get(url, params=payload)
    return response.json()

def is_closed(call):
    return call.get('request_status') == 'Closed'

def generate_closed_calls(limit):
    url = 'https://data.nola.gov/api/id/2jgv-pqrq.json'
    payload = {'$limit': limit}
    

    for call in service_calls(url, payload):
        if not is_closed(call):
            continue
        else:
            yield call

cc = generate_closed_calls(100)

cc

