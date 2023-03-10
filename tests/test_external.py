from unittest.mock import MagicMock
import pytest
from tdd.external import extract_data_from_external_api, ExternalApiError


def test_example():
    assert True
    assert 1 + 1 == 2


def test_api_method_called(mocker):
    get_mock = mocker.patch(
        'tdd.external.requests.get',
        return_value=MagicMock(status_code=200)
    )
    extract_data_from_external_api()
    get_mock.assert_called_with('http://example.com/api/v1/user_data')


def test_error_if_response_status_is_correct(mocker):
    mocker.patch(
        'tdd.external.requests.get',
        return_value=MagicMock(status_code=500)
    )
    with pytest.raises(ExternalApiError):
        extract_data_from_external_api()


def test_return_empty_dict_if_result_is_empty(mocker):
    resp_mock = MagicMock(
        status_code=200,
        json=MagicMock(return_value=[])
    )
    mocker.patch(
        'tdd.external.requests.get',
        return_value=resp_mock
    )
    assert extract_data_from_external_api() == {}


def test_return_correct_summ(mocker):
    resp_mock = MagicMock(
        status_code=200,
        json=MagicMock(
            return_value=[
                {'name': 'Ivan', 'minutes': 10},
                {'name': 'Sergey', 'minutes': 5},
                {'name': 'Maxim', 'minutes': 7},
                {'name': 'Ivan', 'minutes': 10},
                {'name': 'Maxim', 'minutes': 3},
                {'name': 'Ivan', 'minutes': 15},
            ]
        )
    )
    mocker.patch(
        'tdd.external.requests.get',
        return_value=resp_mock
    )

    assert extract_data_from_external_api() == {
        'Ivan': 35,
        'Sergey': 5,
        'Maxim': 10
    }
