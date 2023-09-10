import unittest
import urllib.request as urllib2
import json

class Reader_Base():
    def __init__(self, api_key):
        print("Reader_Base.py:__init__")
        self._api_key = "api_key=" + api_key
        self._api_url = ""  # setting by overrided class.
    def get(self, last_path):
        """
        get api access result.

        Parameters
        ----------
        last_path : str
            api access last path.
        
        Eaxample
        --------
        case : api-summoner access whne search by summoner name.
            self._api_url=https://jp1.api.riotgames.com/lol/summoner/v4/summoners/
            last_path=by-name/[summoner-name]
            api access url = https://jp1.api.riotgames.com/lol/summoner/v4/summoners/by-name/[summoner-name] with api key
        """
        print("Reader_Base.py:get")
        url =  self._create_url(last_path)

        with self._get_url_session(url) as f:
            ret = self._jsonLoad(f,'utf-8')

        return ret

    def _jsonLoad(self, session, character_map):
        """       
        read session to Json.
        """
        print("Reader_Base.py:_jsonLoad")
        return json.loads(session.read().decode(character_map))

    def _get_url_session(self, url):
        """
        open url sesssion.

        Returns
        -------
        opened session.
        """

        print("Reader_Base.py:_get_url_session")
        return urllib2.urlopen(url)
        
    def _create_url(self, lastPath):
        """
        craete api access url.
        """
        print("Reader_Base.py:_create_url")
        url = self._api_url
        url += lastPath
        url += "?"
        url += self._api_key
        return url