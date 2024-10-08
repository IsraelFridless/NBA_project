from repository.database import get_db_connection


def is_players_table_empty() -> bool:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM players;")
        count = cursor.fetchone()
        return count["count"] == 0

def is_seasons_table_empty() -> bool:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM seasons;")
        count = cursor.fetchone()
        return count["count"] == 0

def is_statistics_table_empty() -> bool:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM player_statistics;")
        count = cursor.fetchone()
        return count["count"] == 0