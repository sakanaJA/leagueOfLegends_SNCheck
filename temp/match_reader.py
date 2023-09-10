from . import match_list
from .. import reader_base

class Reader(reader_base.Reader_Base):
    def __init__(self, api_key):
        print("Match.Reader.py:__init__")
        self._api_key = "api_key=" + api_key
        self._api_url = "https://jp1.api.riotgames.com/lol/match/v4/matchlists/"
    
    def get_by_account_id(self, account_id):
        print("Match.Reader.py:get")
        last_path = "by-account/" + account_id

        return match_list.Match_List(self.get(last_path))