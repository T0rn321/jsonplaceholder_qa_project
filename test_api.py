import requests
from faker import Faker

fake = Faker()
# Переключаемся на альтернативное стабильное тренировочное API (JSONPlaceholder)
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_list():
    """Проверка получения списка пользователей (GET)"""
    response = requests.get(f"{BASE_URL}/users")
    
    assert response.status_code == 200, f"Неверный статус код: {response.status_code}"
    json_data = response.json()
    assert len(json_data) > 0, "Список пользователей пуст"
    assert "name" in json_data[0], "В данных пользователя нет ключа 'name'"

def test_create_user_with_fake_data():
    """Проверка создания пользователя со случайными данными (POST)"""
    payload = {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email()
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    assert response.status_code == 201, f"Неверный статус код: {response.status_code}"
    json_data = response.json()
    assert json_data["name"] == payload["name"]
    assert "id" in json_data

def test_update_user():
    """Проверка обновления данных пользователя (PUT)"""
    payload = {
        "name": "Ivan Ivanov",
        "email": "ivan@example.com"
    }
    response = requests.put(f"{BASE_URL}/users/1", json=payload)
    
    assert response.status_code == 200, f"Неверный статус код: {response.status_code}"
    assert response.json()["name"] == payload["name"]

def test_delete_user():
    """Проверка удаления пользователя (DELETE)"""
    response = requests.delete(f"{BASE_URL}/users/1")
    # JSONPlaceholder возвращает 200 OK при успешном удалении
    assert response.status_code == 200, f"Неверный статус код: {response.status_code}"