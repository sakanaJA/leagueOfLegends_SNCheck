from . import match_reference

class Match_List():
    def __init__(self, match_list_dto):
        self._dto = match_list_dto        
        
    @property
    def matches(self):
        ret = []
        for value in self._dto["matches"]:
            ret.append(match_reference.Match_Reference(value))
        return ret

    @property
    def total_games(self):
        return self._dto["totalGames"]

    @property
    def start_index(self):
        return self._dto["startIndex"]

    @property
    def end_index(self):
        return self._dto["endIndex"]    