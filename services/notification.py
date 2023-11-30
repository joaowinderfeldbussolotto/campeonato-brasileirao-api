import requests
from core.config import settings

def notify_goal_on_bot(games):
    try:
        url = settings.BOT_API_URL
        message = ""
        for game in games:
            message += f'{game.home_team} {game.score} {game.away_team}\n'
        data = {"message": message}

        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("POST request successful!")
            print("Response:", response.text)
        else:
            print(f"POST request failed with status code {response.status_code}")
            print("Response:", response.text)
    except Exception:
        return False