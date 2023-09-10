class Info():
    def __init__(self, summoner_dto):
        self._dto = summoner_dto

    @property
    def profile_Icon_Id(self):
        return self._dto["profileIconId"]

    @property
    def name(self):
        return self._dto["name"]

    @property
    def puuid(self):
        return self._dto["puuid"]

    @property
    def summoner_level(self):
        return self._dto["summonerLevel"]

    @property
    def revision_date(self):
        return self._dto["revisionDate"]

    @property
    def id(self):
        return self._dto["id"]

    @property
    def account_id(self):
        return self._dto["accountId"]