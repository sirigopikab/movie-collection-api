import os
import requests

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"


def get_movies(page=1):
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": TMDB_API_KEY,
        "page": page
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        raise Exception("TMDB API Error")

    data = response.json()
    return data.get("results", [])
