import requests
import json
from scripts.logging import error


def op_scraper(query: str) -> dict:
    """
    Call the overpass API and return the response.
    """
    API_URL = "https://overpass-api.de/api/interpreter"
    try:
        response = requests.post(API_URL, data=query)
        if response.status_code == 200:
            return response.json()
    except:
        raise Exception("Overpass API call failed")
