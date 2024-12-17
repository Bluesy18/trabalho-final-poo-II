# trabalho-final-poo-II

´´´
classDiagram
    class User {
        +username: str
        +password: str
        +to_dict()
    }

    class Storage {
        +save_data()
        +load_data()
    }

    class LoginStorage {
        +auth_file: str
        +save_login()
        +load_logins()
    }

    class RentStorage {
        +rent_file: str
        +save_rent()
        +load_rent()
    }

    class Rent {
        +base_url: str
        +api_key: str
        +rent_movie()
    }

    Storage <|-- LoginStorage
    Storage <|-- RentStorage
    RentStorage -- Rent: 0..*
    RentStorage -- User: 0..*
    LoginStorage -- User: 0..*
    User o-- Rent: 0..*
    ´´´
