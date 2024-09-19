from typing import Optional
import repository.team_repository as team_repository
import repository.season_repository as season_repository


def is_valid_team(data) -> bool:
    if len(data['player_ids']) == 0:
        return False
    valid_positions = ['PG', 'SG', 'SF', 'PF', 'C']
    players_positions = [season_repository.get_position_by_player_id(p_id) for p_id in data['player_ids']]
    return set(players_positions) == set(valid_positions)


def create_team(data: dict) -> Optional[int]:
    validated = is_valid_team(data)
    return team_repository.create_team(data) if validated else None