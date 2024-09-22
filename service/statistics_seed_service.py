from repository.player_statistic_repository import add_player_statistics_to_db
from repository.season_repository import get_seasons_from_db
from repository.seed_repository import is_statistics_table_empty
from service.player_statistic_service import get_player_statistics


def seed_statistics():
    if is_statistics_table_empty():
        seasons = get_seasons_from_db()
        for season in seasons:
            player_statistics = get_player_statistics(season.player_id)
            add_player_statistics_to_db(player_statistics)