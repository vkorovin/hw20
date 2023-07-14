from bs4 import BeautifulSoup
import requests
import re
import json
from celery import Celery

app = Celery('tasks', backend='://localhost', broker='pyamqp://guest@localhost//',)
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task
def scarper(url):

    if url.find('?tab=repositories') == -1:
        url += '?tab=repositories'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    main_layout = soup.find_all('a', attrs={'itemprop':'name codeRepository'})
    star_layout = soup.find_all('a',attrs={'href':re.compile("stargazers")})

    stars =dict()
    for star in star_layout:
        stars[star.attrs['href']] = int(star.text)

    result = []
    for data in main_layout:
        item = dict()
        item['url'] = data.attrs['href']
        item['text'] = data.text.strip('\n').lstrip(' ')

        try:
            item['stars'] = stars[data.attrs['href']+'/stargazers']
        except KeyError:
            item['stars'] = 0

        result.append(item)

    return result

if __name__ == '__main__':
    print(scarper(url='https://github.com/jborean93'))
