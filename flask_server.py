from flask import Flask, jsonify, request, render_template
import requests
from functions import *

app = Flask(__name__)

DATES_DICT = {
    'January':[n for n in range(1, 32)],
    'February': [n for n in range(1, 29)],
    'March': [n for n in range(1, 32)],
    'April': [n for n in range(1, 31)],
    'May': [n for n in range(1, 32)],
    'June': [n for n in range(1, 31)],
    'July': [n for n in range(1, 32)],
    'August': [n for n in range(1, 32)],
    'September': [n for n in range(1, 31)],
    'October': [n for n in range(1, 32)],
    'November': [n for n in range(1, 31)],
    'December': [n for n in range(1, 32)]
}

@app.route('/')
def homepage():
    return render_template('meterusage.html', dates=DATES_DICT)

@app.route('/get-data')
def get_data_from_grpc():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # print(get_data(start_date, end_date))
    return "Hi"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")