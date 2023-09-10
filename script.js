const API_KEY = "RGAPI-e1fda35c-deca-4033-8a28-259362f58109";
const BASE_URL = "https://cors-anywhere.herokuapp.com/https://jp1.api.riotgames.com/lol";

function fetchHistory() {
    const summonerName = document.getElementById("summonerName").value;
    fetch(`${BASE_URL}/summoner/v4/summoners/by-name/${summonerName}`, {
        headers: {
            "X-Riot-Token": API_KEY
        }
    })
    .then(response => response.json())
    .then(data => {
        fetch(`${BASE_URL}/match/v4/matchlists/by-account/${data.accountId}`, {
            headers: {
                "X-Riot-Token": API_KEY
            }
        })
        .then(response => response.json())
        .then(matchData => {
            const matchList = document.getElementById("matchList");
            matchList.innerHTML = '';
            matchData.matches.slice(0, 10).forEach(match => {
                const listItem = document.createElement('li');
                listItem.textContent = `Champion ID: ${match.champion}, Role: ${match.role}`;
                matchList.appendChild(listItem);
            });
        });
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
}
