import requests
from config import GOOGLE_MAPS_API_KEY


def get_coordinates(local):
    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": local,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if data["status"] != "OK":
        print("Erro geocode:", data)
        return None

    location = data["results"][0]["geometry"]["location"]

    return location["lat"], location["lng"]



def search_places(lat, lng, tipo, raio=1000):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lng}",
        "radius": raio,
        "type": tipo,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if data["status"] not in ["OK", "ZERO_RESULTS"]:
        print("Erro places:", data)
        return []

    lugares = []

    for place in data.get("results", []):
        lugares.append({
            "nome": place.get("name"),
            "rating": place.get("rating", 0),
            "reviews": place.get("user_ratings_total", 0),
            "lat": place["geometry"]["location"]["lat"],
            "lng": place["geometry"]["location"]["lng"]
        })

    return lugares