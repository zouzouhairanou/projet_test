import unittest

'''import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))'''
from app import app

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_user(self):
        response = self.client.post("/users", json={"name": "Alice"})
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)

    def test_get_user_not_found(self):
        response = self.client.get("/users/999")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
