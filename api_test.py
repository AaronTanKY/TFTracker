import os
import requests
from dotenv import load_dotenv
import json


load_dotenv()


api_key = os.getenv("RIOT_API_KEY")

# Define headers for authorization
headers = {
    "X-Riot-Token": api_key
}

# Replace <region> with one of Riot's platform routing values:
# For example: na1, euw1, kr, etc.
region = "na1"
url = f"https://{region}.api.riotgames.com/tft/league/v1/challenger"

# Make the request
response = requests.get(url, headers=headers)

# Check response
if response.status_code == 200:
    data = response.json()
    json_string = json.dumps(data, indent=4);
    print("Success! Data saved into")
    with open("api_test_data.txt", "w", encoding="utf-8") as f:
        f.write(json_string)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)
