from typing import Optional

from repository.database import get_db_connection


def create_team(data: dict) -> Optional[int]:
    with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO fantasy_teams (team_name, player_ids)
                VALUES (%s, %s)
                RETURNING id;
            ''', (data['team_name'], data['player_ids']))
            new_id = cursor.fetchone()['id']
            connection.commit()
            return new_id