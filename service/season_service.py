from models.season import Season
import repository.season_repository as season_repository


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


def get_players(position, season):
    return season_repository.fetch_players(position, season)

def get_all_player_seasons(player_id: str):
    return season_repository.all_player_seasons(player_id)

def get_two_percent_for_all_seasons(player_id: str):
    return season_repository.two_percent_for_all_seasons(player_id)

def get_three_percent_for_all_seasons(player_id: str):
    return season_repository.three_percent_for_all_seasons(player_id)