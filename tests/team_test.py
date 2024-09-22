from models.season import Season
from repository.season_repository import get_position_by_player_id
import service.team_service as team_service
import repository.team_repository as team_repo
import repository.players_repository as player_repository
import service.season_service as season_service
import service.player_statistic_service as player_statistics_service

def test_create_team():
    team = {
        'team_name': 'test_fake',
        'player_ids': ['griffaj01', 'gordoaa01', 'horfoal01', 'greenaj01', 'holidaa01']
    }
    assert team_service.create_team(team)

def test_is_valid_team():
    team = {
        'team_name': 'test_fake',
        'player_ids': ['griffaj01', 'gordoaa01', 'horfoal01', 'greenaj01', 'holidaa01']
    }
    assert team_service.is_valid_team(team)

def test_get_position_by_player_id():
    assert get_position_by_player_id('griffaj01') == 'SF'

def test_repo_create_team():
    team = {
        'team_name': 'test_fake',
        'player_ids': ['griffaj01', 'gordoaa01', 'horfoal01', 'greenaj01', 'holidaa01']
    }
    assert team_repo.create_team(team) == 4

def test_is_team_exists():
    assert team_service.is_team_exists(3)

def test_validate_team_member():
    assert team_repo.validate_team_member('griffaj01') == True
    assert team_repo.validate_team_member('999') == False
    assert team_repo.validate_team_member('') == False

def test_update_team():
    team = {
        'team_name': 'test_fake',
        'player_ids': ['griffaj01', 'gordoaa01', 'horfoal01', 'greenaj01', 'holidaa01']
    }
    team_id = 2

    updated_team = team_service.update_team(team, team_id)
    assert updated_team is not None
    assert updated_team.team_name == 'test_fake'
    assert updated_team.player_ids == team['player_ids']


def test_get_team_by_id():
    team_id = 2
    fetched_team = team_repo.get_team_by_id(team_id)
    assert fetched_team is not None
    assert fetched_team.team_name == 'test_fake'
    assert fetched_team.player_ids == ['griffaj01', 'gordoaa01', 'horfoal01', 'greenaj01', 'holidaa01']

def test_delete_team():
    team_service.delete_team(2)

def test_get_name_by_id():
    assert isinstance(player_repository.get_name_by_id('griffaj01'), str)

def test_get_player_points_for_all_seasons():
    assert season_service.get_player_points_for_all_seasons('griffaj01') > 0

def test_get_player_games_for_all_seasons():
    assert season_service.get_all_player_games('griffaj01') > 0

def test_get_two_percent_for_all_seasons():
    assert season_service.get_two_percent_for_player('griffaj01') > 0

def test_get_three_percent_for_all_seasons():
    assert season_service.get_three_percent_for_all_seasons('griffaj01') > 0

def test_ppg_player():
    assert player_statistics_service.calculate_player_ppg_ratio_for_all_seasons('griffaj01') > 0

def test_atr_player():
    assert player_statistics_service.calculate_player_atr('griffaj01') > 0

def test_get_seasons_by_player_id():
    seasons = season_service.get_seasons_by_player_id('griffaj01')
    for s in seasons:
        assert isinstance(s, Season)
        assert s.player_id == 'griffaj01'
        assert s.points > 0