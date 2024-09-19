from models import Season
from repository.database import get_db_connection


def create_season(season: Season):
    with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO seasons (player_id, player_name, team, position, season, points, games, turnovers, assists, two_percent, three_percent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (season.player_id, season.player_name, season.team, season.position, season.season, season.points, season.games, season.turnovers, season.assists, season.two_percent, season.three_percent))
            connection.commit()
