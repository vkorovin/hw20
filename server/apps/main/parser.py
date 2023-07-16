import requests
import json
import re
from  bs4 import BeautifulSoup

def ghparser(user):

    result =  requests.get('https://api.github.com/users/{0}/repos'.format(user)).json()

    data = []
    for item in result:
        ditem=dict()

        ditem['url'] = item['html_url']
        ditem['text'] = item['name']
        ditem['stars'] = item['stargazers_count']

        data.append(ditem)

    return data


def ghscarper(name):
    url = "https://github.com/{0}?tab=repositories".format(name)

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    main_layout = soup.find_all('a', attrs={'itemprop': 'name codeRepository'})
    star_layout = soup.find_all('a', attrs={'href': re.compile("stargazers")})

    stars = dict()
    for star in star_layout:
        stars[star.attrs['href']] = int(star.text)

    result = []
    for data in main_layout:
        item = dict()
        item['url'] = data.attrs['href']
        item['text'] = data.text.strip('\n').lstrip(' ')

        try:
            item['stars'] = stars[data.attrs['href'] + '/stargazers']
        except KeyError:
            item['stars'] = 0

        result.append(item)

    return result


if __name__ == '__main__':
    ghparser('elvgarrui')
