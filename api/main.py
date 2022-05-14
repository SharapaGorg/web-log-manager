# local server
from flask import Flask, jsonify, request
from flask_cors import CORS

# logs database interaction
from sqlalchemy import *

# additional tools
from utils import *
from config import LINK
from sys import argv

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

        levels: list = data.get('levels') if data else None
        seconds: list = data.get('seconds') if data else None
        text: str = data.get('text') if data else None
        limit: int = data.get('limit') if data else None
        tablename : str = data.get('tablename') if data else None

        logs = get_logs(database, levels, limit, text, seconds, tablename)

        return jsonify(logs[::-1])
    except Exception as e:
        import traceback
        print(traceback.format_exc(e))
        return 'ERROR'


@app.route('/tables', methods=['GET', 'POST'])
def get_tables_():
    return jsonify(get_tables())


if len(argv) == 1:
    raise Exception('(--dev | --prod) args excepted')

if argv[1] == '--dev':
    app.run(debug=True)

if argv[1] == '--prod':
    app.run(debug=True, host='localhost', port=9001)
