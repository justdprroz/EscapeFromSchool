from flask import Flask, request
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import uuid
import logic

players = {}

@dataclass_json
@dataclass
class Turn:
    gid: str
    index: int

app = Flask(__name__)

@app.route('/do_turn', methods=["POST"])
def do_turn():
    turn = Turn.from_dict(request.json)
    gid = turn.gid
    index = turn.index
    return str(players[gid].doTurn(index))

@app.route('/create_game', methods=["POST"])
def create_room():
    gid = str(uuid.uuid4())
    players[gid] = logic.plotDriver()
    print(players)
    return gid, str(players[gid].getVariants()), str(players[gid].getText())
