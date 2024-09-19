import psycopg2
from psycopg2.extras import RealDictCursor

from config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI, cursor_factory=RealDictCursor)


def create_tables():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS players (
                    player_id VARCHAR(255) PRIMARY KEY,
                    player_name VARCHAR(255) NOT NULL
                );
                CREATE TABLE IF NOT EXISTS seasons (
                    player_id VARCHAR(255) NOT NULL,
                    player_name VARCHAR(255) NOT NULL,
                    team VARCHAR(255) NOT NULL,
                    position VARCHAR(20) NOT NULL,
                    season INT NOT NULL,
                    points INT NOT NULL,
                    games INT NOT NULL,
                    turnovers INT NOT NULL,
                    assists INT NOT NULL,
                    two_percent FLOAT NOT NULL,
                    three_percent FLOAT NOT NULL,
                    CONSTRAINT fk_season_player FOREIGN KEY (player_id) REFERENCES players(player_id)
                );
                CREATE TABLE IF NOT EXISTS player_statistics (
                    player_id VARCHAR(255) PRIMARY KEY,
                    ATR FLOAT NOT NULL,
                    PPGRatio FLOAT NOT NULL,
                    CONSTRAINT fk_stats_player FOREIGN KEY (player_id) REFERENCES players(player_id)
                );
                CREATE TABLE IF NOT EXISTS fantasy_teams (
                    id SERIAL PRIMARY KEY,
                    team_name VARCHAR(255) NOT NULL,
                    player_ids TEXT[]
                );
                """
            )
            connection.commit()


