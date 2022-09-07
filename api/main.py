# local server
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# logs database interaction
from sqlalchemy import *
from database.database import Session

# additional tools
from utils.utils import *
from utils import logger
from sys import argv

app = Flask(__name__)
CORS(app)

try:
    database = Session()
except Exception as e:
    logger.error(f"Problem with connecting to database: {e}")

@app.route('/logs', methods=['GET', 'POST'])
def get_logs_():
    """

    Filter options

    data
        levels
        seconds - range
        text
        limit - count of logs that will be returned
        tablename
        offset
        from_id

    """
    try:
        data = request.get_json()
        session = Session()

        levels = seconds = text = limit = tablename = offset = from_id = None

        if data:
            levels: list = data.get('levels')
            seconds: list = data.get('seconds')
            text: str = data.get('text') 
            limit: int = data.get('limit') 
            tablename : str = data.get('tablename') 
            offset : int = data.get('offset')
            from_id : int = data.get('from_id')

        logs = get_logs(session, levels, limit, text, seconds, tablename, offset, from_id)
        session.close()

        return jsonify(logs[::-1])
    except Exception as e:
        logger.error(e)
        return 'ERROR'


@app.route('/', methods=['GET'])
def docs():
    return open(os.path.join('..', 'docs.html'), 'r').read()

@app.route('/tables', methods=['GET', 'POST'])
def get_tables_():
    return jsonify(get_tables())

@app.route('/last', methods=['GET', 'POST'])
def get_last():
    """
    
    returns last element id

    """
    try:
        data = request.get_json()
        tablename = None
        session = Session()

        if data:
            tablename : str = data.get('tablename')

        result = str(get_last_id(session, tablename))
        session.close()

        return result
    except Exception as e:
        logger.error(f'[get_last] {e}')
        return 'ERROR'

@app.route('/generate_log', methods=['POST'])
def generate_log_():
    """
    
    tablename : str
    content : str
    level : str

    """
    data = request.get_json()
    session = Session()

    table_name : str = data.get('tablename')
    content : str = data.get('content')
    log_level : str = data.get('level')

    try:
        log = generate_log(session, table_name, log_level, content)
    except Exception as e:
        return str(e), 400

    # session.close()

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
