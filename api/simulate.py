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
tables, status_code = logger.get_tables()

print('AVAILABLE TABLES: ', tables)

# get logs from table
for table in tables:
    logs, status_code = logger.get_logs(table)
    print(f'[{table}] LOGS COUNT: ', len(logs))

# generate log and add to table
table_name = 'SUCK'
log_level = 'WARNING'
content = 'Core module messed up all'

log, status_code = logger.generate_log(table_name, content, log_level)
print(log)