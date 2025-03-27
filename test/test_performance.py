from locust import HttpUser, task, between

class UserTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_users(self):
        self.client.get("/users")

    @task
    def create_user(self):
        self.client.post("/users", json={"name": "TestUser"})
