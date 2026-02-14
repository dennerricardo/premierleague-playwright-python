leaderboard_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "playerMetadata": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "position": {"type": "string"},
                            "country": {
                                "type": "object",
                                "properties": {
                                    "country": {"type": "string"}
                                },
                                "required": ["country"]
                            },
                            "currentTeam": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"}
                                },
                                "required": ["name"]
                            }
                        },
                        "required": ["name", "position", "country", "currentTeam"]
                    },
                    "stats": {
                        "type": "object",
                        "properties": {
                            "goals": {"type": "number"}
                        },
                        "required": ["goals"]
                    }
                },
                "required": ["playerMetadata", "stats"]
            }
        }
    },
    "required": ["data"]
}