from repository.database import create_tables
from service.players_seed_service import seed_players
from service.season_seed_service import seed_seasons
from service.statistics_seed_service import seed_statistics


def test_seed_database():
    create_tables()
    seed_players()
    seed_seasons()
    seed_statistics()
