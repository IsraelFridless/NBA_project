
from api.nba_api_data import get_data
from repository.players_repository import create_player
from repository.seed_repository import is_players_table_empty
from service.player_service import convert_to_player


def seed_players():
    if is_players_table_empty():
        data = get_data()
        for obj in data:
            player = convert_to_player(obj)
            create_player(player)
