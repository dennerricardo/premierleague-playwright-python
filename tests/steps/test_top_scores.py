import json
import requests

url = str (
        "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v3/"
        "competitions/8/seasons/2025/players/stats/leaderboard"
        "?_sort=goals:desc&country=&_limit=10"
    )

def test_top_scores(api_request_context):

    response = requests.get(url)
    print(response)

    # Validate response
    response.raise_for_status()

    # Print the status code
    status_code = response.status_code
    print(status_code)

    # Print formatted JSON in terminal
    data = response.json()
    print(json.dumps(data, indent=2))


def test_can_call_endpoin():
    response = requests.get(url)
    status_code = response.status_code
    print(status_code)
    assert response.status_code == 200
    pass


def test_prints_new_json():

    response = requests.get(url)

    # with open("players_leaderboard_2025.json", "w", encoding="utf-8") as file:
    #     json.dump(data, file, indent=2, ensure_ascii=False)

    # print("JSON file created successfully!")