from datetime import datetime

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "created_at": self.created_at
        }
 