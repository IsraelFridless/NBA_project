from flask import Blueprint, request, jsonify
import service.team_service as team_service
teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route('/', methods=['POST'])
def create_team():
    request_data = request.json
    team_data: dict = {**request_data}
    team_name = team_data.get('team_name')
    player_ids = team_data.get('player_ids')
    if not team_name or not player_ids:
        return jsonify({'Error': 'Invalid team data. Please provide a team name and a list of player IDs.'}), 400
    new_team_id = team_service.create_team(team_data)
    if not new_team_id:
        return jsonify({'Error': 'Failed to create a new team. Please check the provided data.'}), 400
    return jsonify({'message': f'Successfully created the team. Team ID: {new_team_id}'}), 201
