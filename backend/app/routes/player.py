from app import app
from ..views import player


@app.route("/players", methods=["GET"])
def get_players():
    return player.get_players()

@app.route("/player/<id>", methods=["GET"])
def get_player(id):
    return player.get_player(id)

@app.route("/player/register", methods=["POST"])
def register_player():
    return player.register()

@app.route("/player/login", methods=["POST"])
def login_player():
    return player.login()