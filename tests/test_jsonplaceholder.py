import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_posts():
    """Тест на получение всех постов"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_get_single_post():
    """Тест на получение конкретного поста"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert 'id' in response.json()
    assert response.json()['id'] == 1


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user(user_id):
    """Тест на получение постов конкретного пользователя"""
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_create_post():
    """Тест на создание нового поста"""
    data = {
        "title": "test",
        "body": "test",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.status_code == 201
    assert 'id' in response.json()


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_post(post_id):
    """Тест на удаление поста"""
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
