"""

Using :

python simulate.py count

count - count of logs, which will be generated

"""

from sys import argv
from API import Logger

API_KEY = 'SOME'
count = 10

if len(argv) > 1:
    count = int(argv[1])

# logger object
logger = Logger(API_KEY)

# get tables
tables = logger.get_tables()

# get logs from table
logs = logger.get_logs('some')
print(logs)

# generate log and add to table
pass