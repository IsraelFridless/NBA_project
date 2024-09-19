from models.Season import Season
from models.player_statistics import PlayerStatistics
from repository.player_statistic_repository import get_position_average


def get_atr(season: Season) -> float:
    return season.assists if season.turnovers == 0 else season.assists / season.turnovers

def get_ppg_ratio(season: Season) -> float:
    points_per_game = season.points / season.games
    position_average = get_position_average(season.position)
    return float(points_per_game) / float(position_average)

def get_player_statistics(season: Season) -> PlayerStatistics:
    atr = get_atr(season)
    ppg_ratio = get_ppg_ratio(season)
    return PlayerStatistics(player_id=season.player_id, ATR=atr, PPGRatio=ppg_ratio)
