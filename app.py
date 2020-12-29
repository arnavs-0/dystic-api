import json
from flask import Flask, request, Response
from jobScrape_script import *
from intlScrape_script import *
from moreDetailsScrape_script import *

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/jobs', methods=["GET"])
def welcome():
    if request.method == "GET":
        if 'jt' in request.args and 'jl' in request.args:
            jobTitle = request.args['jt']
            jobLocation = request.args['jl']

            data = jobScrape(jobTitle, jobLocation)
            # print(type(data))
            return data
        else:
            return '''{"success": false, "reason": "jt (job type), jl (job location) is required"}'''
    else:
        return "Please call this URL as an API"


@app.route('/intl', methods=["GET"])
def intl():
    if request.method == "GET":
        if 'jt' in request.args and 'jl' in request.args and 'jc' in request.args:
            jobTitle = request.args['jt']
            jobLocation = request.args['jl']
            jobCountry = request.args['jc']

            data = intlScrape(jobCountry, jobTitle, jobLocation)
            # print(type(data))
            return data
        else:
             return '''{"success": false, "reason": "jt (job type), jl (job location), and jc (job country) is required"}''' 
    else:
        return "Please call this URL as an API"
@app.route('/details', methods=["GET"])
def details():
    if request.method == "GET":
        if 'ju' in request.args:
            url = request.args['ju']
            data = get_details(url)
            return data
        else:
            return '''{"success": false, "reason": "job url (ju) is required"}'''
    else:
        return "Must be a GET request"

@app.route('/')
def home():
    return """
    <h1>dystic API</h1>
    <h2>Endpoints</h2>
    <li>/jobs</li>
    <li>/intl</li>
    <li>/details</li>
    <h5>&copy dystic 2020-2021</h5>
    """


if __name__ == '__main__':
    app.run(debug=True)
