"""

Using :

python simulate.py count

count - count of logs, which will be generated

"""

from utils import *
from config import LINK
from sqlalchemy import *
from time import sleep
from sys import argv
from requests import post

count = 10

if len(argv) > 1:
    count = int(argv[1])

database = create_session(LINK)
target_table = get_table('logs1')

def generate_log_(table_name : str):
    api = 'http://127.0.0.1:5000/generate_log'

    log = post(api, json={
        'tablename' : table_name
    })

    return log

for i in range(count):
    log = generate_log_('logs1')
    print(log.text)
    
    sleep(.5)

