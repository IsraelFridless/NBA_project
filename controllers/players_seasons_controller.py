from service.player_statistic_service import calculate_player_atr, calculate_player_ppg_ratio_for_all_seasons


from flask import Blueprint, request, jsonify
import service.season_service as season_service
import repository.player_statistic_repository as player_statistics_repo

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route('/', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    if not position:
        return jsonify({"error": "'position' parameters is required"}), 400
    seasons = season_service.get_players(position, season)
    return jsonify([
        {
             'player_id': s.player_id,
             'playerName': s.player_name,
             'team': s.team,
             'position': s.position,
             'seasons': season_service.get_all_player_seasons(s.player_id),
             'points': s.points,
             'games': s.games,
             'two_percent': season_service.get_two_percent_for_all_seasons(s.player_id),
             'three_percent': season_service.get_three_percent_for_all_seasons(s.player_id),
             'ATR': player_statistics_repo.get_player_atr(s.player_id),
             'PPG_ratio': player_statistics_repo.get_player_ppg(s.player_id)
         } for s in seasons])
