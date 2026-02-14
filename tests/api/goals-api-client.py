import requests

def get_players_leaderboard(api_request_context):
    url = (
        "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v3/"
        "competitions/8/seasons/2025/players/stats/leaderboard"
    )
    params = {
        "_sort": "goals:A desc",
        "country": "",
        "_limit": limit,
    }
    if next_cursor:
        params["_next"] = next_cursor

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    print(data)

    return data