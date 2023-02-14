import requests


class ExternalApiError(Exception):
    pass


def extract_data_from_external_api():
    requests.get('http://example.com/api/v1/user_data')
