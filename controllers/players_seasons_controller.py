from service.player_statistic_service import get_atr, get_ppg_ratio


from flask import Blueprint, request, jsonify
import service.season_service as season_service

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
             'ATR': get_atr(s),
             'PPG_ratio': get_ppg_ratio(s)
         } for s in seasons])
