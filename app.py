from flask import Flask
app = Flask(__name__)
@app.route('/jobs', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500)