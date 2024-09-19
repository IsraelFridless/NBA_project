from typing import List

from models.season import Season
from repository.database import get_db_connection


def create_season(season: Season):
    with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO seasons (player_id, player_name, team, position, season, points, games, turnovers, assists, two_percent, three_percent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (season.player_id, season.player_name, season.team, season.position, season.season, season.points, season.games, season.turnovers, season.assists, season.two_percent, season.three_percent))
            connection.commit()


def get_seasons_by_position_and_season(position: str, season: str = None) -> List[Season]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        if season:
            cursor.execute('SELECT * FROM seasons WHERE position = %s AND season = %s', (position, season))
        else:
            cursor.execute('SELECT * FROM seasons WHERE position = %s', (position,))

        seasons = cursor.fetchall()
        return [Season(**s) for s in seasons]

def all_player_seasons(player_id: str) -> List[int]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT DISTINCT season
            FROM seasons
            WHERE player_id = %s
            ORDER BY season;
        ''', (player_id,))
        seasons = cursor.fetchall()
        print(f"Fetched seasons: {seasons}")  # Debugging print
        return [season['season'] for season in seasons]

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
