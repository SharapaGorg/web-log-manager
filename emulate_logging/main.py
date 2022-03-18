# local server
from flask import Flask, jsonify
from flask_cors import CORS

# logs database interaction
from sqlalchemy import *

# additional tools
from utils import *
from config import LINK

from json import dumps

database = create_session(LINK)

app = Flask(__name__)

CORS(app)

@app.route('/logs')
def get_routes():
    logs = get_logs(database)

    # return dumps(logs, indent=4, sort_keys=True)
    return jsonify(logs)

app.run(debug=True)