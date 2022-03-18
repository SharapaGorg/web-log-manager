# local server
from flask import Flask, jsonify, request
from flask_cors import CORS

# logs database interaction
from sqlalchemy import *

# additional tools
from utils import *
from config import LINK

database = create_session(LINK)

app = Flask(__name__)

CORS(app)

@app.route('/logs', methods=['GET', 'POST'])
def get_logs_():
    """
    
    Filter options
    
    data
        levels
        time
        seconds
        text
        limit - count of logs that will be returned

    """
    data = request.get_json()

    levels = data.get('levels')
    time = data.get('time')
    seconds = data.get('seconds')
    text = data.get('text')
    limit = data.get('limit')

    logs = get_logs(database, levels=levels, limit=limit)

    return jsonify(logs)



app.run(debug=True)