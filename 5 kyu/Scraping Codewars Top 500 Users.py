from bs4 import BeautifulSoup
import requests


def parser():
    url = 'https://www.codewars.com/users/leaderboard'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    users = soup.find('div', attrs={'class': 'leaderboard p-0'}).find(
        'table').find_all("tr")
    bigmass = []
    for i in range(1, 501):
        user = users[i]['data-username']
        clan_honor = users[i].find_all('td')
        clan = clan_honor[2].text
        honor = int(clan_honor[3].text.replace(',', ''))
        bigmass.append(User(user, honor, clan))
    return bigmass


class MyList(list):

    def __init__(self, I):
        super().__init__(I)

    def __getitem__(self, item):
        return list.__getitem__(self, item - 1)


class solution:
    def __init__(self):
        self.position = MyList(parser())

    def __getitem__(self, iterm):
        return self.position[iterm - 1]


class User:
    def __init__(self, name, honor, clan=''):
        self.name = name
        self.honor = honor
        self.clan = clan
