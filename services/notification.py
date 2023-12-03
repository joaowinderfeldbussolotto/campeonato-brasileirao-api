import pika
import json
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
    
def notify_queue(games):

    games = [dict(game) for game in games]
    server, queue = settings.SERVER, settings.QUEUE
    connection = pika.BlockingConnection(pika.ConnectionParameters(server))
    channel = connection.channel()
    channel.queue_declare(queue)

    channel.basic_publish(exchange='', routing_key=queue, body=json.dumps({"data": games}))


    connection.close()
