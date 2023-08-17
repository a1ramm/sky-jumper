from app import db, ma, fields

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    coins = db.Column(db.Integer, nullable=False)


class PlayerSchema(ma.Schema):
    class Meta:
        model = Player
    id = fields.Integer()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    score = fields.Integer()
    coins = fields.Integer()

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)