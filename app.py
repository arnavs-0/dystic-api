import json
from flask import Flask, request, Response
from jobScrape_script import *
from intlScrape_script import *

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/jobs', methods=["GET"])
def welcome():
    if request.method == "GET":
        jobTitle = request.args['jt']
        jobLocation = request.args['jl']

        data = jobScrape(jobTitle, jobLocation)
        # print(type(data))
        return data
    else:
        return "Please call this URL as an API"

@app.route('/intl', methods=["GET"])
def intl():
    if request.method == "GET":
        jobTitle = request.args['jt']
        jobLocation = request.args['jl']
        jobCountry = request.args['jc']

        data = intlScrape(jobCountry, jobTitle, jobLocation)
        # print(type(data))
        return data
    else:
        return "Please call this URL as an API"

@app.route('/')
def home():
    return """
    <h1>dystic API</h1>
    <h2>Endpoints</h2>
    <li>/jobs</li>
    <li>/intl</li>
    <h5>&copy dystic 2020-2021</h5>
    """


if __name__ == '__main__':
    app.run(debug=True)
