from collections import defaultdict
import requests


class ExternalApiError(Exception):
    pass


def extract_data_from_external_api():
    resp = requests.get('http://example.com/api/v1/user_data')
    if resp.status_code != 200:
        raise ExternalApiError('Response status code is invalid')

    resp_json = resp.json()
    if resp_json == []:
        return {}

    agg = defaultdict(lambda: 0)
    for item in resp_json:
        agg[item['name']] += item['minutes']

    return agg
