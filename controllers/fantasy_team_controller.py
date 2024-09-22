from typing import Optional, List
import service.player_service as player_service
from flask import Blueprint, request, jsonify
import service.team_service as team_service
from models.FantasyTeam import FantasyTeam
import service.season_service as season_service
import repository.player_statistic_repository as player_statistics_repo

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route('/', methods=['POST'])
def create_team():
    request_data = request.json
    team_data: dict = {**request_data}
    team_name = team_data.get('team_name')
    player_ids = team_data.get('player_ids')
    if not team_name or not player_ids:
        return jsonify({'Error': 'Invalid team data. Please provide a team name and a list of player IDs.'}), 400
    try:
        new_team: FantasyTeam = team_service.create_team(team_data)
        return jsonify({'message': 'Successfully created the team.', 'new_team': new_team}), 201
    except Exception as e:
        return jsonify({'Error': f'{e}'}), 400


@teams_blueprint.route('/<team_id>', methods=['PUT'])
def update_team(team_id: int):
    if not team_service.is_team_exists(team_id):
        return jsonify({"error": f"Team id {team_id} does not exists"}), 400
    request_data = request.json
    team_data: dict = {**request_data}
    team_name = team_data.get('team_name')
    player_ids = team_data.get('player_ids')
    if not team_name or not player_ids:
        return jsonify({'Error': 'Invalid team data. Please provide a team name and a list of player IDs.'}), 400
    try:
        updated_team: Optional[FantasyTeam] = team_service.update_team(team_data, team_id)
        return jsonify({'message': 'Successfully updated the team.', 'updated_team': updated_team}), 200
    except Exception as e:
        return jsonify({'Error': f'{e}'}), 400

@teams_blueprint.route('/<team_id>', methods=['DELETE'])
def delete_team(team_id: int):
    try:
        team_service.delete_team(team_id)
        return jsonify({'message': f'Successfully deleted the team by id {team_id}.'}), 200
    except Exception as e:
        return jsonify({'Error': f'{e}'}), 400

@teams_blueprint.route('/compare', methods=['GET'])
def compare_teams_by_ids():
    team_ids = request.args.getlist('team_id', type=int)
    if not team_ids:
        return jsonify({"error": "No team IDs provided"}), 400
    try:
        teams_sorted_by_ppg: List[FantasyTeam] = team_service.sort_teams_by_ppg(team_ids)
        return jsonify([
            {
                 'team': team.team_name,
                 'points': team_service.get_team_points(team),
                 'two_percent': team_service.get_two_percent_for_team(team),
                 'three_percent': team_service.get_three_percent_for_all_team(team),
                 'ATR': team_service.get_atr_for_all_team(team),
                 'PPG_ratio': team_service.get_ppg_ratio_for_all_team(team)
             } for team in teams_sorted_by_ppg])
    except Exception as e:
        return jsonify({'Error': f'{e}'}), 400

@teams_blueprint.route('/<team_id>', methods=['GET'])
def get_team_details(team_id: int):
    if not team_id:
        return jsonify({"error": "No team ID provided"}), 400
    team = team_service.get_team_by_id(team_id)
    if not team:
        return jsonify({"error": f"Team by if {team_id} does not exists"}), 400
    try:
        return jsonify({
            'team_name': team.team_name,
            'players': [{
                'playerName': player_service.get_player_name_by_id(p_id),
                'team': team.team_name,
                'position': season_service.get_position_by_player_id(p_id),
                'points': season_service.get_player_points_for_all_seasons(p_id),
                'games': season_service.get_all_player_games(p_id),
                'twoPercent': season_service.get_two_percent_for_player(p_id),
                'threePercent': season_service.get_three_percent_for_all_seasons(p_id),
                'ATR': player_statistics_repo.get_player_atr(p_id),
                'PPG Ratio': player_statistics_repo.get_player_ppg(p_id)
            } for p_id in team.player_ids]
        })
    except Exception as e:
        return jsonify({'Error': f'{e}'}), 400