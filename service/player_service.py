from models.Player import Player


def convert_to_player(obj: dict) -> Player:
    return Player(
        obj['playerId'],
        obj['playerName'])