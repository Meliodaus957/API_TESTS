import requests



# Тестовая функция для проверки статуса ответа
def test_check_url_status(url, status_code):

    response = requests.get(url)

    # Проверяем, что статус-код совпадает с ожидаемым
    assert response.status_code == status_code, f"Ожидал {status_code}, получил {response.status_code}"
