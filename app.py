from flask import Flask, request, redirect, jsonify
from jobScrape_script import *
from urllib.parse import unquote
# from intlScrape_script import *
from moreDetailsScrape_script import *
from getCountry import getCountryCode
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
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
            # return json.loads(data), int(json.loads(data)['statusCode'])
            return data
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
            # url = request.args['ju']
            # data = get_details(url)
            # return data
            i = request.args['ju']
            url = unquote(i)
            data = get_details('https://www.indeed.com/viewjob?cmp=Partech&t=Firmware+Developer&jk=b925a17f21aaf1fe&sjdu=QwrRXKrqZ3CNX5W-O9jEvbCKnmXEzLyMBrs3gIHlNWvJbQpQHi5BoRvr8e22IUJUpvoV9mAYHLyXl8MR08Y-XQ&adid=312389480&ad=-6NYlbfkN0Cq2a5lNafOK06dKo-7gXGxOSr25-80nMAj1uySNMa9z3ZPhdc3Ln2Kdy5h4SJN6YGCSpkYB1ZryPXuYumXTrZcZ-GSVckAZnDkRG0WUCkT94VV0f1Uy3YVjDlXPBnodAVlTl9pER0ZLBvd1bzQhKbLGO683rptijIKK15_phakk8z4jpThonc12IsSrn3dxz2mIkRxjEfYOR0crRhl5Rl9fqwzVHpWfOv9vEiCLNhC2risj2lszTAtwhI-gtUI8bLgO0322ltTM_hWhw3AbCTnbdysQps2IgBnOLzdJyh1PLXuZ1_B8DNXXHQKP1cmONU%3D&pub=4a1b367933fd867b19b072952f68dceb&vjs=3')
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
