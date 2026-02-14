import json

import requests
from tests.utils.player_mapper import PlayerMapper

BASE_URL = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v3"
ENDPOINT = "/competitions/8/seasons/2025/players/stats/leaderboard"

PARAMS = {
    "_sort": "goals:desc",
    "country" : "",
    "_limit": 100
}


def get_leaderboard():
    print(f"\nGET: {BASE_URL}{ENDPOINT}")
    response = requests.get(f"{BASE_URL}{ENDPOINT}", params=PARAMS)
    response.raise_for_status()
    return response


def generate_players_json():
    print(f"\nGET: {BASE_URL}{ENDPOINT}")
    response = requests.get(f"{BASE_URL}{ENDPOINT}", params=PARAMS)
    data = response.json()

    mapper = PlayerMapper()
    players = mapper.extract_player(data)

    with open("players_score_2025_26.json", "w", encoding="utf-8") as file:
        json.dump(players, file, indent=2, ensure_ascii=False)

    print("JSON file created successfully!")
    return players

