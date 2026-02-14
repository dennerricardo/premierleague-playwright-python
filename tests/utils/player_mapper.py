class PlayerMapper :

    def extract_player(self, data):
        players = []
        for p in data["data"]:
            players.append({
                "name": p["playerMetadata"]["name"],
                "country": p["playerMetadata"]["country"]["country"],
                "position": p["playerMetadata"]["position"],
                "team": p["playerMetadata"]["currentTeam"]["name"],
                "goals": p["stats"]["goals"]
            })
        return players


