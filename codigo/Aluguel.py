import requests



class Rent:
    base_url = "http://www.omdbapi.com/?"
    api_key = "13e83016"

    def rent_movie(name):
        params = {
            "apikey": Rent.api_key,
            "t": name
        }

        try:
            response = requests.get(Rent.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            filtered_data = data["Title"]["Year"]["Genre"]
            return filtered_data
        
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
