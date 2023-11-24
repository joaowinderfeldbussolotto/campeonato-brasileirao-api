import requests
from bs4 import BeautifulSoup
import re
from models.game import Game
from models.round import Round


def scrap_rounds(url = 'https://www.cbf.com.br/futebol-brasileiro'):

    rounds = []
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    results = soup.select('.aside-content .clearfix')

    home = []
    away = []
    score = []

    for element in results:
        home_abbr = element.select_one('.pull-left .time-sigla').get_text()
        away_abbr = element.select_one('.pull-right .time-sigla').get_text()

        # Check if the team abbreviation is 'COR' and the title starts with 'Coritiba'
        if home_abbr == 'COR' and element.select_one('img[title^="Coritiba"]'):
            home_team = 'CFC'
        else:
            home_team = home_abbr

        home.append(home_team)
        away.append(away_abbr)

        score_text = element.select_one('.partida-horario').get_text()
        score_value = re.search(r'\d{1} x \d{1}', score_text)
        score.append(score_value.group() if score_value else 'Ainda não aconteceu!')


    num_rounds = len(home)
    rounds_per_dict = 10
    for i in range(0, num_rounds, rounds_per_dict):
        key = (i // rounds_per_dict) + 1
        games = []
        for j in range(i, i+rounds_per_dict):
            game = Game(home_team= home[j], away_team = away[j], score = score[j])
            games.append(game)
        round = Round(number = key, games = games)
        rounds.append(round)
    return rounds


def format_round(rounds, number):
    games = []
    for i in range(10):
        print(rounds['home'][i], rounds['away'][i], rounds['score'][i])
        home_team, away_team, score = rounds['home'][i], rounds['away'][i], rounds['score'][i]
        game = Game(home_team= home_team, away_team = away_team, score = score)
        games.append(game)

    return Round(number = number, games = games)