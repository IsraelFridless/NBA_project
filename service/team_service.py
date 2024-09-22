from statistics import mean
from typing import Optional, List

from toolz import pipe
from toolz.curried import partial
import service.player_statistic_service as player_statistics_service
import repository.player_statistic_repository as player_statistics_repo
import repository.team_repository as team_repository
import service.season_service as season_service
from models.FantasyTeam import FantasyTeam


def is_valid_team(team_data: dict) -> bool:
    if len(team_data['player_ids']) < 5:
        return False
    valid_positions = ['PG', 'SG', 'SF', 'PF', 'C']
    players_positions = [season_service.get_position_by_player_id(p_id) for p_id in team_data['player_ids']]
    return set(players_positions) == set(valid_positions)

def create_team(team_data: dict) -> FantasyTeam:
    validated = is_valid_team(team_data)
    if not validated:
        raise Exception('Team is not valid because one or more of the place are placed in the same position')
    new_team_id: int = team_repository.create_team(team_data)
    fantasy_team: Optional[FantasyTeam] = team_repository.get_team_by_id(new_team_id)
    if not fantasy_team:
        raise Exception('could not fetch the the team for some reason')
    return fantasy_team

def is_team_exists(team_id: int) -> bool:
    return team_repository.get_team_by_id(team_id) is not None

def is_valid_player(player_id: str) -> bool:
    is_valid = team_repository.validate_team_member(player_id)
    return is_valid

def update_team(team_data: dict, team_id: int) -> Optional[FantasyTeam]:
    valid_team: bool = is_valid_team(team_data)
    is_valid_players: bool = pipe(
        team_data['player_ids'],
        partial(map, lambda player_id: is_valid_player(player_id)),
        all
    ) if valid_team else False

    if not is_valid_players:
        raise Exception('No valid players')

    try:
        team_repository.update_team(team_data, team_id)
        updated_team = team_repository.get_team_by_id(team_id)
        return updated_team

    except Exception as e:
        print(f"Error updating team: {e}")
        return None

def delete_team(team_id: int):
    team_repository.delete_team(team_id)

def sort_teams_by_ppg(team_ids: List[int]) -> List[FantasyTeam]:
    teams: List[FantasyTeam] = pipe(
        team_ids,
        partial(map, team_repository.get_team_by_id),
        list
    )
    if None in teams:
        raise Exception('one or more of the teams does not exists in the database')
    return sorted(teams, key=get_ppg_ratio_for_all_team, reverse=True)

def get_team_points(team: FantasyTeam) -> int:
    return pipe(
        team.player_ids,
        partial(map, player_statistics_service.get_player_points),
        list,
        sum
    )

def get_two_percent_for_team(team) -> float:
    return pipe(
        team.player_ids,
        partial(map, player_statistics_service.get_player_two_percent),
        list,
        mean
    )

def get_three_percent_for_all_team(team) -> float:
    return pipe(
        team.player_ids,
        partial(map, player_statistics_service.get_player_three_percent),
        list,
        mean
    )

def get_atr_for_all_team(team) -> float:
    return pipe(
        team.player_ids,
        partial(map, player_statistics_repo.get_player_atr),
        list,
        mean
    )

def get_ppg_ratio_for_all_team(team) -> float:
    return pipe(
        team.player_ids,
        partial(map, player_statistics_repo.get_player_ppg),
        list,
        mean
    )

def get_team_by_id(team_id: int) -> Optional[FantasyTeam]:
    return team_repository.get_team_by_id(team_id)