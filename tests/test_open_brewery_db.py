import pytest
import requests



BASE_URL = "https://api.openbrewerydb.org/breweries"


def test_get_all_breweries():
    """Тест на получение всех пивоварен"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_get_brewery_by_id():
    """Тест на получение информации о конкретной пивоварне по ID"""
    response = requests.get(f"{BASE_URL}/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0")
    assert response.status_code == 200
    assert 'name' in response.json()
    assert response.json()['name'] == "MadTree Brewing 2.0"


@pytest.mark.parametrize("city", ["San Diego", "New York", "Chicago"])
def test_get_breweries_by_city(city):
    """Тест на фильтрацию пивоварен по городу"""
    response = requests.get(BASE_URL, params={"by_city": city})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    for resp_info in response.json():
        assert city in resp_info.get('city'), f'Expected {city} in {resp_info}'


@pytest.mark.parametrize("state", ["California", "New York"])
def test_get_breweries_by_state(state):
    """Тест на фильтрацию пивоварен по штату"""
    response = requests.get(BASE_URL, params={"by_state": state})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_search_brewery_by_name():
    """Тест на поиск пивоварен по имени"""
    response = requests.get(BASE_URL, params={"by_name": "dog"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
