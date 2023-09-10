from flask import Flask, render_template, request
import requests

app = Flask(__name__)

RIOT_API_KEY = 'RGAPI-20398309-fd70-486d-9e07-b284bcca418b'  # このキーはセキュリティのため公開しないようにしてください
BASE_URL = "https://jp1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
MATCH_HISTORY_BASE_URL = "https://jp1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
MATCH_DETAIL_BASE_URL = "https://jp1.api.riotgames.com/lol/match/v4/matches/"

def get_summoner_data(summoner_name):
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }
    response = requests.get(BASE_URL + summoner_name, headers=headers)
    return response

def get_match_history(account_id, limit=5):
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }
    params = {
        'endIndex': limit  # 最新の5試合の履歴を取得
    }
    response = requests.get(MATCH_HISTORY_BASE_URL + account_id, headers=headers, params=params)
    return response.json()

def get_match_detail(game_id):
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }
    response = requests.get(MATCH_DETAIL_BASE_URL + str(game_id), headers=headers)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    match_history = None
    match_details = []

    if request.method == 'POST':
        summoner_name = request.form['summoner_name']
        summoner_data_response = get_summoner_data(summoner_name)
        
        if summoner_data_response.status_code == 200:
            summoner_data = summoner_data_response.json()
            account_id = summoner_data['accountId']
            
            match_history = get_match_history(account_id)
            
            for match in match_history["matches"]:
                detail = get_match_detail(match["gameId"])
                match_details.append(detail)
            
            return render_template('index.html', summoner_data=summoner_data, match_history=match_history, match_details=match_details)
        else:
            return render_template('index.html', error="データの取得に失敗しました。", summoner_data=None, match_history=None, match_details=None)

    return render_template('index.html', summoner_data=None, match_history=None, match_details=None)

if __name__ == '__main__':
    app.run(debug=True)
