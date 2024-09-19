from service.player_statistic_service import get_atr, get_ppg_ratio


from flask import Blueprint, request, jsonify
from repository.season_repository import get_seasons_by_position_and_season, all_player_seasons, two_percent_for_all_seasons, three_percent_for_all_seasons

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route('/', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    if not position:
        return jsonify({"error": "'position' parameters is required"}), 400
    seasons = get_seasons_by_position_and_season(position, season)
    return jsonify([
        {
             'playerName': s.player_name,
             'team': s.team,
             'position': s.position,
             'seasons': all_player_seasons(s.player_id),
             'points': s.points,
             'games': s.games,
             'two_percent': two_percent_for_all_seasons(s.player_id),
             'three_percent': three_percent_for_all_seasons(s.player_id),
             'ATR': get_atr(s),
             'PPG_ratio': get_ppg_ratio(s)
         } for s in seasons])
