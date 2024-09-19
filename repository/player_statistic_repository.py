from typing import List

from models.Season import Season
from models.player_statistics import PlayerStatistics
from repository.database import get_db_connection


def get_position_average(position: str) -> float:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT AVG(points) AS avg_points
                FROM seasons
                WHERE position = %s
            ''', (position,))
            avg_points = cursor.fetchone()
            return avg_points["avg_points"]
def add_player_statistics_to_db(player_statistics: PlayerStatistics):
    with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO player_statistics (player_id, ATR, PPGRatio)
                VALUES (%s, %s, %s)
                ON CONFLICT (player_id) DO NOTHING
            ''', (player_statistics.player_id, player_statistics.ATR, player_statistics.PPGRatio))
            connection.commit()

def get_seasons_from_db() -> List[Season]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('SELECT * FROM seasons')
        seasons = cursor.fetchall()
        return [Season(**s) for s in seasons]