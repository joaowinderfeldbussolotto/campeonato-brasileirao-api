from unidecode import unidecode
import requests
from bs4 import BeautifulSoup
from models.game import Game
from utils import helper

def clean_data(list):
    leagues = (['Brazilian Série A'])
    list = [i[-145:] for i in list]
    left, right = '">', '</'
    list = [[l[l.index(left)+len(left):l.index(right)] for l in list if i in l] for i in leagues][0]
    return list


def format_live_games_scraping(scraped_data):
  scraped_data = scraped_data[1:]
  games = []

  for i in range(0, len(scraped_data), 5):
      score = 'Ainda não aconteceu!' if '' in scraped_data[i:i+5] else f"{scraped_data[i+1]} x {scraped_data[i+3]}"
      home_team, away_team = process_team_name(scraped_data[i]), process_team_name(scraped_data[i+2])
      game = Game(home_team=home_team, away_team=away_team, score=score)
      games.append(game)
  return games

        
def scrap_live_games():
    
    url = "https://www.bbc.com/sport/football/scores-fixtures/2023-11-22"
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html.parser")
        
    tags = ["span", "h3"]
    classes = (["gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc",
                  "sp-c-fixture__status-wrapper qa-sp-fixture-status",
                  'sp-c-fixture__number sp-c-fixture__number--time', "sp-c-fixture__number sp-c-fixture__number--home",
                  "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft",
                 "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live-sport",
                  "sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--live-sport",
                 "sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--ft",
                  'gel-minion sp-c-match-list-heading'])

    scraper = soup.find_all(tags, attrs={'class': classes})
    data = clean_data([str(item) for item in scraper])
    return format_live_games_scraping(data)



def process_team_name(team_name):
    processed_name = unidecode(team_name).upper()
    return processed_name[:3]