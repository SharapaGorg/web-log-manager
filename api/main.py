# local server
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# logs database interaction
from sqlalchemy import *

# additional tools
from utils.utils import *
from utils import logger
from config import LINK
from sys import argv

app = Flask(__name__)

CORS(app)
database = create_session(LINK)

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
        data = request.get_json()

        levels: list = data.get('levels') if data else None
        seconds: list = data.get('seconds') if data else None
        text: str = data.get('text') if data else None
        limit: int = data.get('limit') if data else None
        tablename : str = data.get('tablename') if data else None

        logs = get_logs(database, levels, limit, text, seconds, tablename)

        return jsonify(logs[::-1])
    except Exception as e:
        logger.error(e)
        # import traceback
        # print(traceback.format_exc(e))
        return 'ERROR'


@app.route('/', methods=['GET'])
def docs():
    return open(os.path.join('..', 'docs.html'), 'r').read()

@app.route('/tables', methods=['GET', 'POST'])
def get_tables_():
    return jsonify(get_tables())

@app.route('/generate_log', methods=['POST'])
def generate_log_():
    """
    
    tablename : str
    content : str
    level : str

    """
    data = request.get_json()

    table_name : str = data.get('tablename')
    content : str = data.get('content')
    log_level : str = data.get('level')

    try:
        log = generate_log(database, table_name, log_level, content)
    except Exception as e:
        return str(e), 400

    return jsonify({
        'id' : log.id,
        'time' : log.time,
        'level' : log.level,
        'text' : log.text
    })


if len(argv) == 1:
    raise Exception('(--dev | --prod) args excepted')

if argv[1] == '--dev':
    app.run(debug=True)

if argv[1] == '--prod':
    app.run(debug=True, host='localhost', port=9001)
