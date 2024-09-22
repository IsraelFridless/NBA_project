from typing import Optional
from models.FantasyTeam import FantasyTeam
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


def validate_team_member(player_id: str) -> bool:
    if not player_id:
        return False
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            SELECT EXISTS (
                SELECT 1
                FROM fantasy_teams
                WHERE %s = ANY(player_ids)
            ) AS is_exists;
        ''', (player_id,))
        result = cursor.fetchone()
        return result['is_exists'] if result else False


def get_team_by_id(team_id: int) -> Optional[FantasyTeam]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('SELECT * FROM fantasy_teams WHERE id = %s;', (team_id,))
        result = cursor.fetchone()
        return FantasyTeam(team_name=result['team_name'], player_ids=result['player_ids'], id=result['id']) if result else None


def update_team(team_data: dict, team_id: int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            UPDATE fantasy_teams
            SET team_name = %s, player_ids = %s
            WHERE id = %s;
        ''', (team_data.get('team_name'), team_data.get('player_ids'), team_id))
        connection.commit()


def delete_team(team_id: int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            'DELETE FROM fantasy_teams WHERE id = %s RETURNING id;',
            (team_id,)
        )
        deleted_team_id = cursor.fetchone()
        if deleted_team_id is None:
            raise Exception(f"Team with ID {team_id} does not exist.")
        connection.commit()