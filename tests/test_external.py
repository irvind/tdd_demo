from unittest.mock import MagicMock
import pytest
from tdd.external import extract_data_from_external_api, ExternalApiError


def test_example():
    assert True
    assert 1 + 1 == 2


def test_api_method_called(mocker):
    get_mock = mocker.patch('tdd.external.requests.get')
    extract_data_from_external_api()
    get_mock.assert_called_with('http://example.com/api/v1/user_data')


def test_error_if_response_status_is_correct(mocker):
    mocker.patch(
        'tdd.external.requests.get',
        return_value=MagicMock(status_code=500)
    )
    with pytest.raises(ExternalApiError):
        extract_data_from_external_api()
