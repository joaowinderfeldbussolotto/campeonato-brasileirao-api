import requests
from bs4 import BeautifulSoup
import re



def scrap_rounds(url = 'https://www.cbf.com.br/futebol-brasileiro'):

    rounds = {}
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    results = soup.select('.aside-content .clearfix')

    home = [element.select_one('.pull-left .time-sigla').get_text() for element in results]
    away = [element.select_one('.pull-right .time-sigla').get_text() for element in results]
    score = [re.search(r'\d{1} x \d{1}', element.select_one('.partida-horario').get_text()).group()
            if element.select_one('.partida-horario') is not None and re.search(r'\d{1} x \d{1}', element.select_one('.partida-horario').get_text()) is not None
            else 'Ainda não aconteceu!'
            for element in results]

    num_rounds = len(results)
    rounds_per_dict = 10

    for i in range(0, num_rounds, rounds_per_dict):
        key = (i // rounds_per_dict) + 1
        rounds[key] = {'home': home[i:i+rounds_per_dict],
                        'away': away[i:i+rounds_per_dict],
                        'score': score[i:i+rounds_per_dict]}
        
    return rounds


