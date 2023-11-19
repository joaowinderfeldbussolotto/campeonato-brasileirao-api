import requests
from bs4 import BeautifulSoup


def scrap_table(url: str = 'https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/'):

    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    standings_table = soup.find('table')

    table = []

    for row in standings_table.find_all('tr')[1:]:
        columns = row.find_all('td')
        team_name = columns[2].text.strip()
        classification = int(columns[0].text.strip())
        points = int(columns[4].text.strip())
        games_played = int(columns[5].text.strip())

        team_data = {
            'team': team_name.replace('>>','').strip(),
            'position': classification,
            'points': points,
            'games_played': games_played
        }

        table.append(team_data)

    return table