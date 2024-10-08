
from flask import Flask

from controllers.fantasy_team_controller import teams_blueprint
from controllers.players_seasons_controller import players_blueprint

app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(players_blueprint, url_prefix="/api/players")
    app.register_blueprint(teams_blueprint, url_prefix="/api/teams")
    app.run(debug=True)