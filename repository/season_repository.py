from typing import List, Optional

from models.season import Season
from repository.database import get_db_connection


def create_season(season: Season):
    with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO seasons (player_id, player_name, team, position, season, points, games, turnovers, assists, two_percent, three_percent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (season.player_id, season.player_name, season.team, season.position, season.season, season.points, season.games, season.turnovers, season.assists, season.two_percent, season.three_percent))
            connection.commit()

def get_position_by_player_id(player_id: str) -> str:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT position as position
            FROM seasons
            WHERE player_id = %s;
            ''', (player_id,))
        result = cursor.fetchone()
        return result['position']

def fetch_players(position: str, season: str = None) -> List[Season]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        if season:
            cursor.execute('SELECT * FROM seasons WHERE position = %s AND season = %s', (position, int(season)))
        else:
            cursor.execute('SELECT * FROM seasons WHERE position = %s', (position,))

        seasons = cursor.fetchall()
        return [Season(**s) for s in seasons]

def two_percent_for_all_seasons(player_id: str) -> float:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT AVG(two_percent) as total_two_percent
            FROM seasons
            WHERE player_id = %s;
        ''', (player_id,))
        result = cursor.fetchone()
        return result['total_two_percent']

def three_percent_for_all_seasons(player_id: str) -> float:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT AVG(three_percent) as total_three_percent
            FROM seasons
            WHERE player_id = %s;
        ''', (player_id,))
        result = cursor.fetchone()
        return result['total_three_percent']

# function to fetch all the seasons of a specific player => List[Season]
def get_player_seasons(player_id) -> List[Season]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM seasons
            WHERE player_id = %s
        ''', (player_id,))
        seasons = cursor.fetchall()
        return [Season(**s) for s in seasons]


def get_player_points_for_all_seasons(player_id: str) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT SUM(points) as total_points
            FROM seasons
            WHERE player_id = %s;
        ''', (player_id,))
        result = cursor.fetchone()
        return result['total_points']


def get_all_player_games(player_id: str) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT SUM(games) as total_games
            FROM seasons
            WHERE player_id = %s;
        ''', (player_id,))
        result = cursor.fetchone()
        return result['total_games']

def get_seasons_from_db() -> List[Season]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('SELECT * FROM seasons')
        seasons = cursor.fetchall()
        return [Season(**s) for s in seasons]

def get_position_average_points(position: str) -> float:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT AVG(points) AS avg_points
                FROM seasons
                WHERE position = %s
            ''', (position,))
            avg_points = cursor.fetchone()
            return avg_points["avg_points"]