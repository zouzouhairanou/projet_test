import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

def test_add_user():
    response = requests.post(f"{BASE_URL}/users", json={"name": "Bob"})
    assert response.status_code == 201

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_delete_user():
    response = requests.post(f"{BASE_URL}/users", json={"name": "Charlie"})
    user_id = response.json().get("id", 2)  # Simuler l'ID
    delete_response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert delete_response.status_code == 200
