"""

Using :

python simulate.py count

count - count of logs, which will be generated

"""

from sys import argv
from utils.API import Logger
from faker import Faker
import random
import json

API_KEY = 'SOME'

count = 10
faker = Faker('en_US')

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
levels = ['WARNING', 'INFO', 'DEBUG', 'ERROR']

for i in range(count):
    table_name = 'logs1'
    log_level = random.choice(levels)
    content = faker.sentence(random.randint(4, 12))

    log, status_code = logger.generate_log(table_name, content, log_level)
    print(json.dumps(log, indent=4, sort_keys=True))