import requests

class Rent:
    base_url = "http://www.omdbapi.com/?"
    api_key = "13e83016"

    @staticmethod
    def rent_movie(name):
        params = {
            "apikey": Rent.api_key,
            "t": name
        }

        try:
            response = requests.get(Rent.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("Response") == "True":  
                filtered_data = {
                    "Title": data["Title"],
                    "Year": data["Year"],
                    "Genre": data["Genre"],
                    "PricePerDay": 15
                }
                return filtered_data
            else:
                return {"error": data.get("Error", "Filme não encontrado.")}

        
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
