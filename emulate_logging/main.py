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

    levels = data.get('levels') if data else None
    time = data.get('time') if data else None
    seconds = data.get('seconds') if data else None
    text = data.get('text') if data else None
    limit = data.get('limit') if data else None

    logs = get_logs(database, levels=levels, limit=limit, text=text)

    return jsonify(logs[::-1])



# dev
app.run(debug=True)
# prod
app.run(debug=True, host='localhost', port=9001)