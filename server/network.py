from flask import Flask, request
from dataclasses import dataclass
from dataclasses_json import dataclass_json

template = ["sheesh", "yowza"]

@dataclass_json
@dataclass
class Turn:
    index: int

app = Flask(__name__)

@app.route('/do_turn', methods=["POST"])
def do_turn():
    turn = Turn.from_dict(request.json)
    index = turn.index
    return template[index]
