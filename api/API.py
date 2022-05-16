from requests import get, post
from json import loads

class Logger:
    __API__ = 'http://127.0.0.1:5000/'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_tables(self, **options) -> list:
        source = 'tables'

        return loads(get(self.__API__ + source).text)


    def get_logs(self, 
                table_name : str, 
                content : str = None,
                log_level : str = None,
                time : str = None,
                **options) -> list:
        source = 'logs'

        api_request = post(self.__API__ + source, json = {
            
        })

        return api_request.text

    def generate_log(self,
                     content: str,
                     log_level: str,
                     time: str,
                     **options) -> bool:


        source = 'generate_log'


