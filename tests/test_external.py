from tdd.external import extract_data_from_external_api


def test_example():
    assert True
    assert 1 + 1 == 2


def test_api_method_called(mocker):
    get_mock = mocker.patch('tdd.external.requests.get')
    extract_data_from_external_api()
    get_mock.assert_called_with('http://example.com/api/v1/user_data')
