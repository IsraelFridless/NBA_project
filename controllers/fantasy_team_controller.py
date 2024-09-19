from flask import Blueprint

fantasy_blueprint = Blueprint("fantasy", __name__)

@fantasy_blueprint.route('/users/<int:question_id>', methods=['GET'])
def get_players_by_position(position: str, season: int):
    pass