from models.Player import Player
import repository.players_repository as players_repository

def convert_to_player(obj: dict) -> Player:
    return Player(
        obj['playerId'],
        obj['playerName'])


def get_player_name_by_id(player_id: str) -> str:
    return players_repository.get_name_by_id(player_id)