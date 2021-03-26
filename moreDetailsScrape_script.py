import json
import requests
from requests.api import get
from bs4 import BeautifulSoup

def get_details(url): 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        logo = soup.find('img', 'jobsearch-JobInfoHeader-logo').get('src')
    except AttributeError:
        logo = 'https://upload.wikimedia.org/wikipedia/commons/a/a0/Circle_-_black_simple.svg'
    
    try:
        title = soup.find('h1', 'jobsearch-JobInfoHeader-title').text.strip()
    except AttributeError:
        title = 'Why this dumb'
    
    company = soup.find('div', 'icl-u-lg-mr--sm').text.strip()

    rate = soup.find("meta",  itemprop="ratingValue")
    rating = rate["content"] 

    link = soup.find('div', 'icl-u-lg-hide').a
    apply = link.get('href')
    job_desc = soup.find('div', 'jobsearch-jobDescriptionText').text

    return json.dumps({"success": "true", "logo": logo, "title": title, "company": company, "applyUrl": apply, "description": job_desc, "rating": rating})




    

