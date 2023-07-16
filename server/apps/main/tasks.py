from bs4 import BeautifulSoup
import requests
import re
#import json,urllib.request
from celery import Celery
from .parser import ghparser

app = Celery('tasks', backend='://localhost', broker='pyamqp://guest@localhost//',)
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task
def parser(name):
    return ghparser(name)

#def ghparser(user):
#
#    output =   urllib.request.urlopen('https://api.github.com/users/{0}/repos'.format(user)).read()
#    result  = json.loads(output)
#    data = []
#    for  value in result:
#        ditem = dict()
#        ditem['url'] = value.get('html_url')
#        ditem['text'] = value.get('name')
#        ditem['stars'] = value.get('stargazers_count')

 #       data.append(ditem)

  #  return data

@app.task
def scarper(url):

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
    print(ghparser('elvgarrui'))

