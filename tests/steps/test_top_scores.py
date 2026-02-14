import json
from  tests.utils.goals_api_client import get_leaderboard

def test_can_call_endpoint():
    response = get_leaderboard()
    print(f"STATUS CODE : {response.status_code}" )
    assert response.status_code == 200


def test_top10_scores(players_file):
    with open("players_score_2025_26.json", encoding="utf-8") as f:
        data = json.load(f)

    print("\n===========================================================================")
    print(f"{'Player':<21} | {'Team':<25} | Goals")
    print("==========================================================================")

    for player in data[:10]:
        assert "name" in player
        assert "team" in player
        assert "goals" in player
        print(f"{player['name']:<21} | {player['team']:<25}  | {player['goals']} ")




