# local server
from flask import Flask, jsonify, request
from flask_cors import CORS

# logs database interaction
from sqlalchemy import *

# additional tools
from utils import *
from config import LINK

app = Flask(__name__)

CORS(app)

@app.route('/logs', methods=['GET', 'POST'])
def get_logs_():
    """

    Filter options

    data
        levels
        seconds - range
        text
        limit - count of logs that will be returned

    """
    try:
        database = create_session(LINK)
        data = request.get_json()

        levels : list = data.get('levels') if data else None
        seconds : list = data.get('seconds') if data else None
        text : str = data.get('text') if data else None
        limit : int = data.get('limit') if data else None

        logs = get_logs(database, levels, limit, text, seconds)

        return jsonify(logs[::-1])
    except:
        return 'ERROR'



# dev
app.run(debug=True)
# prod
app.run(debug=True, host='localhost', port=9001)
