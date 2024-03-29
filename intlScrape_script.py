import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

template = 'https://{}.indeed.com/jobs?q={}&l={}'


def get_url(country, position, location):
    template = 'https://{}.indeed.com/jobs?q={}&l={}'
    url = template.format(country, position, location)
    return url


# noinspection DuplicatedCode
def get_record(country, card):
    atag = card.h2.a
    job_title = atag.get('title')

    job_url = 'https://' + country + '.indeed.com' + atag.get('href')

    company = card.find('span', 'company').text.strip()

    location = card.find('div', 'recJobLoc').get('data-rc-loc')

    try:
        remote = card.find('span', 'remote').text.strip()
    except AttributeError:
        remote = 'Not Remote'

    summary = card.find('div', 'summary').text.strip()

    date_post = card.find('span', 'date').text.strip()

    date_today = datetime.today().strftime('%Y-%m-%d')

    try:
        salary = card.find('span', 'salaryText').text.strip()
    except AttributeError:
        salary = ''

    record = (job_title, job_url, company, location, remote, summary, date_post, date_today, salary)
    return record


def intlScrape(country, position, location):
    records = []
    url = get_url(country, position, location)

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'jobsearch-SerpJobCard')

        for card in cards:
            record = get_record(country, card)
            records.append(record)

        try:
            url = 'https://' + country + '.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break

    if records:
        return json.dumps(
            [{"statusCode": 200, "JobTitle": x[0], "JobUrl": x[1], "Company": x[2], "Location": x[3], "Remote": x[4],
              "Summary": x[5], "PostDate": x[6], "ExtractDate": x[7], "Salary": x[8]} for x in records],
            indent=1)
    else:
        return json.dumps({"success": False, "statusCode": 400, "reason": "No job was found with given request"})
