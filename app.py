import json
from flask import Flask, request, jsonify, Response
from jobScrape_script import *

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/jobs', methods=["GET"])
def welcome():
    if request.method == "GET":
        data = jobScrape('Android Developer', 'Detroit, MI')
        # print(type(data))
        return data
    else:
        return "Please call this URL as an API"


if __name__ == '__main__':
    app.run(debug=True)
