import requests
from core.config import settings

def notify_goal_on_bot(games):
    try:
        url = settings.BOT_API_URL
        games = [dict(game) for game in games]
        data = {"data": games}

        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("POST request successful!")
            print("Response:", response.text)
        else:
            print(f"POST request failed with status code {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(str(e))
        return False