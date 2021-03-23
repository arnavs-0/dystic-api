from flask import Flask, request, redirect, jsonify
from jobScrape_script import *
# from intlScrape_script import *
from moreDetailsScrape_script import *
from getCountry import getCountryCode

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# http://127.0.0.1:5000/jobs?jt=construction&jl=waterloo&jn=physical
@app.route('/jobs', methods=["GET"])
def welcome():
    if request.method == "GET":
        jobTitle = request.args['jt']
        jobLocation = request.args['jl']
        jobType = request.args['jn']
        if 'jt' in request.args and 'jl' in request.args and 'jn':
            data = jobScrape(jobTitle, jobLocation, jobType)
            return json.loads(data), int(json.loads(data)['statusCode'])
        else:
            return json.dumps({"success": False, "reason": "jt (job type), jl (job location) is required"}), 500
    else:
        return "Please call this URL as an API"


#
# @app.route('/intl', methods=["GET"])
# def intl():
#     if request.method == "GET":
#         if 'jt' in request.args and 'jl' in request.args and 'jc' in request.args:
#             jobTitle = request.args['jt']
#             jobLocation = request.args['jl']
#             jobCountry = request.args['jc']
#
#             data = intlScrape(jobCountry, jobTitle, jobLocation)
#             # print(type(data))
#             return data
#         elif 'jc' not in request.args:
#             jobTitle = request.args['jt']
#             jobLocation = request.args['jl']
#             jobCountry = defaultCountryCode
#
#             data = intlScrape(jobCountry, jobTitle, jobLocation)
#             # print(type(data))
#             return data
#         else:
#             return json.dumps({"success": False, "reason": "jt (job type), jl (job location) is required"})
#     else:
#         return "Please call this URL as an API"


@app.route('/details', methods=["GET"])
def details():
    if request.method == "GET":
        if 'ju' in request.args:
            url = request.args['ju']
            data = get_details(url)
            return data
        else:
            return json.dumps({"success": False, "reason": "jt (job type), jl (job location) is required"})
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
