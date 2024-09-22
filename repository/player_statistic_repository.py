from models.player_statistics import PlayerStatistics
from repository.database import get_db_connection


def add_player_statistics_to_db(player_statistics: PlayerStatistics):
    with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO player_statistics (player_id, ATR, PPGRatio)
                VALUES (%s, %s, %s)
                ON CONFLICT (player_id) DO NOTHING
            ''', (player_statistics.player_id, player_statistics.ATR, player_statistics.PPGRatio))
            connection.commit()

def get_player_ppg(player_id: str) -> float:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT PPGRatio AS ppg
                FROM player_statistics
                WHERE player_id = %s
            ''', (player_id,))
            result = cursor.fetchone()
            return result["ppg"]

def get_player_atr(player_id: str) -> float:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT ATR AS atr
                FROM player_statistics
                WHERE player_id = %s
            ''', (player_id,))
            result = cursor.fetchone()
            return result["atr"]