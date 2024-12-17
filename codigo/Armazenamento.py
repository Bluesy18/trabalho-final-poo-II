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
    
class RentStorage(Storage):
    def __init__(self):
        self.rent_file = "alugueis.json"

    
    def save_rent(self, user, rent_info):
        all_rents = self.load_data(self.rent_file) or {}
        if user not in all_rents:
            all_rents[user] = []
        all_rents[user].append(rent_info)
        self.save_data(self.rent_file, all_rents)

    def load_rents(self, user):
        all_rents = self.load_data(self.rent_file) or {}
        return all_rents.get(user, [])


