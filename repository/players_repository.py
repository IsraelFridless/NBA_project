from models.Player import Player
from repository.database import get_db_connection


def create_player(player: Player):
    with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO players (player_id, player_name)
                VALUES (%s, %s)
                ON CONFLICT (player_id) DO NOTHING
            ''', (player.player_id, player.player_name))
            connection.commit()

