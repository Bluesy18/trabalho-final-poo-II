import json
from datetime import datetime

class Storage:
    def save_data(self, filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return None

class LoginStorage(Storage):
    def __init__(self):
        self.auth_file = "users.json"

    def save_login(self, users):
        self.save_data(self.auth_file, users)

    def load_logins(self):
        return self.load_data(self.auth_file) or {}