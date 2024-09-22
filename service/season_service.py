from typing import Optional, List

from toolz import pipe
from toolz.curried import partial

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

def get_all_player_seasons(player_id: str) -> List[int]:
    seasons = season_repository.get_player_seasons(player_id)
    return pipe(
        seasons,
        partial(map, lambda season: season.season),
        list
    )

def get_player_points_for_all_seasons(player_id: str) -> int:
    return season_repository.get_player_points_for_all_seasons(player_id)

def get_two_percent_for_all_seasons(player_id: str):
    return season_repository.two_percent_for_all_seasons(player_id)

def get_three_percent_for_all_seasons(player_id: str):
    return season_repository.three_percent_for_all_seasons(player_id)

def get_seasons_by_player_id(player_id) -> List[Season]:
    seasons = season_repository.get_player_seasons(player_id)
    return seasons

def get_position_by_player_id(player_id: str) -> str:
    return season_repository.get_position_by_player_id(player_id)


def get_all_player_games(player_id: str) -> int:
    return season_repository.get_all_player_games(player_id)

def get_two_percent_for_player(player_id: str) -> float:
    return season_repository.two_percent_for_all_seasons(player_id)