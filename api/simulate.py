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

count = 10

if len(argv) > 1:
    count = int(argv[1])

database = create_session(LINK)

for i in range(count):
    log = generate_log(database)
    print(log.level, log.text)
    
    sleep(.5)

