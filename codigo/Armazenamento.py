import json

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
    
class RentStorage:
    def load_rents(self, username):
        data = self.load_all_data()
        return data.get(username, [])

    def save_rent(self, username, rent):
        data = self.load_all_data()
        if username not in data:
            data[username] = []
        data[username].append(rent)
        self.save_all_data(data)

    def save_all_rents(self, username, rents):
        data = self.load_all_data()
        data[username] = rents
        self.save_all_data(data)

    def load_all_data(self):
        try:
            with open('rents_data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_all_data(self, data):
        with open('rents_data.json', 'w') as file:
            json.dump(data, file, indent=4)



