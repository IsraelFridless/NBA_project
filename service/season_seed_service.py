from api.nba_api_data import get_data
from repository.season_repository import create_season
from repository.seed_repository import is_seasons_table_empty
from service.season_service import convert_to_season


def seed_seasons():
    if is_seasons_table_empty():
        data = get_data()
        for obj in data:
            season = convert_to_season(obj)
            create_season(season)

