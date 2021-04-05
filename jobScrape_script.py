from datetime import datetime
import json
import flask
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.api import get
from bs4 import BeautifulSoup
from keywords import match
from getCountry import getCountryCode
from citiesDictionary import getUSCities
import sys
import geocoder


defaultCountryCode = getCountryCode().lower()
allUSCities = getUSCities()

# if defaultCountryCode == 'us':
#     template = 'https://www.indeed.com/jobs?q={}&l={}'
# else:
#     template = 'https://' + defaultCountryCode + '.indeed.com/jobs?q={}&l={}'
template = 'https://www.indeed.com/jobs?q={}&l={}'


def get_url(position, location):
    url = template.format(position, location)
    return url


def get_record(card, jobtype):
    atag = card.h2.a
    job_title = atag.get('title')

    if defaultCountryCode == 'us':
        urlHead = 'https://indeed.com'
    else:
        urlHead = 'https://www.' + defaultCountryCode + '.indeed.com'

    job_url = urlHead + atag.get('href')
    print('Hello world!', file=sys.stderr)

    company = card.find('span', 'company').text.strip()

    location = card.find('div', 'recJobLoc').get('data-rc-loc')
    g = geocoder.arcgis(location)
    latlng = g.latlng

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
    # TODO Fix this record thing which returns null
    if match(jobtype, job_title) or match(jobtype, summary):
        record = (job_title, job_url, company, location, remote, summary, date_post, date_today, salary, latlng)
    else:
        record = ('n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a')

    return record


def jobScrape(position, location, jobtype):
    records = []
    url = get_url(position, location)

    while True:
        try:
           
            response = requests.get(url)
            print(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('div', 'jobsearch-SerpJobCard')

            for card in cards:
                record = get_record(card, jobtype)
                records.append(record)
            break

            # try:
            #     if defaultCountryCode == 'us':
            #         urlHead = 'https://indeed.com'
            #     else:
            #         urlHead = 'https://' + defaultCountryCode + '.indeed.com'

            #     url = urlHead + soup.find('a', {'aria-label': 'Next'}).get('href')
            # except AttributeError:
            #     break
        except requests.exceptions.ConnectionError as e:
            return json.dumps({"success": False, "statusCode": 500, "reason": "Connection refused by the server",
                               "solution": "Please try again in a few minutes", "details": str(e)})

   
    return json.dumps(
        [{"statusCode": 200, "JobTitle": x[0], "JobUrl": x[1], "Company": x[2], "Location": x[3], "Remote": x[4],
            "Summary": x[5], "PostDate": x[6], "ExtractDate": x[7], "Salary": x[8], "LatLng": x[9]} for x in records],
        indent=1)
