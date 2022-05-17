from requests import get, post
from json import loads

class Logger:
    __API__ = 'http://127.0.0.1:5000/'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_tables(self, **options) -> list:
        source = 'tables'

        req = get(self.__API__ + source)

        try:
            return loads(req.text), req.status_code
        except:
            return req.text, req.status_code

    def get_logs(self,
                 table_name: str,
                 content: str = None,
                 levels: list = None,
                 time: str = None,
                 limit : int = None,
                 **options) -> list:

        source = 'logs'

        req = post(self.__API__ + source, json={
            'levels' : levels,
            'seconds' : time,
            'text' : content,
            'tablename' : table_name,
            'limit' : limit
        })

        try:
            return loads(req.text), req.status_code
        except:
            return req.text, req.status_code

    def generate_log(self,
                     table_name : str,
                     content: str,
                     log_level: str,
                     **options) -> dict:

        source = 'generate_log'

        req = post(self.__API__ + source, json = {
            'tablename' : table_name,
            'content' : content,
            'level' : log_level
        })

        try:
            return loads(req.text), req.status_code
        except:
            return req.text, req.status_code
