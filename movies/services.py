import os
import requests
from requests.auth import HTTPBasicAuth
from tenacity import retry, stop_after_attempt, wait_fixed


MOVIE_API_URL = "https://demo.credy.in/api/v1/maya/movies/"


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetch_movies(url=None):
    username = os.getenv("MOVIE_API_USERNAME")
    password = os.getenv("MOVIE_API_PASSWORD")

    if not username or not password:
        raise Exception("Movie API credentials not set")

    response = requests.get(
        url or MOVIE_API_URL,
        auth=HTTPBasicAuth(username, password),
        timeout=15
    )
    response.raise_for_status()
    return response.json()
