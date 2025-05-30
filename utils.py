import os
import requests
from dotenv import load_dotenv
import json

# Load whatever is in the .env file
load_dotenv()

# Read the api key
API_KEY = os.getenv("RIOT_API_KEY")

# Define headers for authorization
HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_top_players_puuids(region):
    url = f"https://{region}.api.riotgames.com/tft/league/v1/challenger"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return [entry["puuid"] for entry in data["entries"][:50]]

def get_match_ids_for_puuid(region, puuid):
    url = f"https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=20"
    response = requests.get(url, headers=HEADERS)
    return response.json()