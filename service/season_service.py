from models.season import Season


def convert_to_season(obj: dict) -> Season:
    return Season(
        obj['playerId'],
        obj['playerName'],
        obj['team'],
        obj['position'],
        obj['season'],
        obj['points'] or 0,
        obj['games'] or 0,
        obj['turnovers'],
        obj['assists'] or 0,
        obj['twoPercent'] or 0,
        obj['threePercent'] or 0)