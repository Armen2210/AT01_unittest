import pytest
from main_AT03_mocking import get_weather
from main_AT03_mocking import get_github_user
from main_AT03_mocking import get_cat_picture


def test_get_weather_success(mocker):
    mock_get = mocker.patch('main_AT03_mocking.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 25}
    }

    api_key = 'e3855e2108bb797d9cb8e1f093419970'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 25}
    }

def test_get_weather_error(mocker):
    mock_get = mocker.patch('main_AT03_mocking.requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'e3855e2108bb797d9cb8e1f093419970'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data is None

def test_get_github_user_success(mocker):
    mock_get = mocker.patch('main_AT03_mocking.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login' : 'nizavr',
        'id' : 345178,
        'name' : 'Nina'
    }

    user_data = get_github_user('nizavr')
    assert user_data == {
        'login' : 'nizavr',
        'id' : 345178,
        'name' : 'Nina'
    }

def test_get_github_user_error(mocker):
    mock_get = mocker.patch('main_AT03_mocking.requests.get')
    mock_get.return_value.status_code = 404

    user_data = get_github_user('nizavr')
    assert user_data is None


def test_get_cat_picture_success(mocker):
    mock_get = mocker.patch('main_AT03_mocking.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'url' : 'https://example.com/cat.jpg'
    }

    cat_api_key = 'live_J2WcZBGT0uMnijSjiJxw9pXpiPqLuvBNkcDdlgbmEf2yftlUNtgaGipzTTNB2hC5'
    cat_picture = get_cat_picture(cat_api_key)
    assert cat_picture == {'url': 'https://example.com/cat.jpg'}

def test_get_cat_picture_error(mocker):
    mock_get = mocker.patch('main_AT03_mocking.requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {
        'url' : 'https://example.com/cat.jpg'
    }

    cat_api_key = 'live_J2WcZBGT0uMnijSjiJxw9pXpiPqLuvBNkcDdlgbmEf2yftlUNtgaGipzTTNB2hC5'
    cat_picture = get_cat_picture(cat_api_key)
    assert cat_picture == None

