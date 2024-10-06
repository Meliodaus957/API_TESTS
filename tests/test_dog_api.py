import pytest
import requests



BASE_URL = "https://dog.ceo/api"


def test_get_random_image():
    """Тест на получение случайного изображения собаки"""
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200
    assert 'message' in response.json()
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize("breed", ["hound", "retriever", "terrier"])
def test_get_images_by_breed(breed):
    """Тест на получение изображений по породе"""
    response = requests.get(f"{BASE_URL}/breed/{breed}/images")
    assert response.status_code == 200
    assert 'message' in response.json()
    assert len(response.json()['message']) > 0


def test_list_all_breeds():
    """Тест на получение списка всех пород"""
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    assert 'message' in response.json()
    assert len(response.json()['message']) > 0


@pytest.mark.parametrize("sub_breed", ["bulldog/english", "retriever/golden"])
def test_get_sub_breed_images(sub_breed):
    """Тест на получение изображений по под-породам"""
    response = requests.get(f"{BASE_URL}/breed/{sub_breed}/images")
    assert response.status_code == 200
    assert 'message' in response.json()
    assert len(response.json()['message']) > 0


def test_get_random_image_by_breed():
    """Тест на получение случайного изображения по породе"""
    response = requests.get(f"{BASE_URL}/breed/hound/images/random")
    assert response.status_code == 200
    assert 'message' in response.json()
    assert response.json()['status'] == 'success'
