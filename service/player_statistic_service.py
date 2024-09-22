from statistics import mean
from typing import List

from toolz import pipe
from toolz.curried import partial

import service.season_service as season_service
from models.season import Season
from models.player_statistics import PlayerStatistics
from repository.season_repository import get_position_average_points


def calculate_player_atr(player_id: str) -> float:
    seasons: List[Season] = season_service.get_seasons_by_player_id(player_id)
    assists = sum([s.assists for s in seasons])
    turnovers = sum([s.turnovers for s in seasons])
    return assists if turnovers == 0 else assists / turnovers


def calculate_player_ppg_ratio_for_all_seasons(player_id: str) -> float:
    seasons: List[Season] = season_service.get_seasons_by_player_id(player_id)

    total_points = sum(season.points for season in seasons)
    total_games = sum(season.games for season in seasons if season.games > 0)
    points_per_game = total_points / total_games if total_games > 0 else 0.0

    # Calculate positional averages for each season
    position_averages = [get_position_average_points(season.position) for season in seasons]
    position_average = mean(position_averages) if position_averages else 0.0

    # Return 0.0 if position average is 0 to avoid division by zero
    if position_average == 0:
        return 0.0

    # Return the PPG ratio
    return float(points_per_game) / float(position_average)


def get_player_statistics(player_id: str) -> PlayerStatistics:
    atr = calculate_player_atr(player_id)
    ppg_ratio = calculate_player_ppg_ratio_for_all_seasons(player_id)
    return PlayerStatistics(player_id=player_id, ATR=atr, PPGRatio=ppg_ratio)

def get_player_points(player_id: str) -> int:
    seasons: List[Season] = season_service.get_seasons_by_player_id(player_id)
    return pipe(
        seasons,
        partial(map, lambda season: season.points),
        sum
    )

def get_player_two_percent(player_id: str) -> float:
    seasons: List[Season] = season_service.get_seasons_by_player_id(player_id)
    return pipe(
        seasons,
        partial(map, lambda season: season.two_percent),
        mean
    )

def get_player_three_percent(player_id: str) -> float:
    seasons: List[Season] = season_service.get_seasons_by_player_id(player_id)
    return pipe(
        seasons,
        partial(map, lambda season: season.three_percent),
        mean
    )