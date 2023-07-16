import requests
import json

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


if __name__ == '__main__':
    ghparser('elvgarrui')
