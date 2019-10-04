from flask import Flask, flash, jsonify, request, render_template, redirect, session
from datetime import datetime
import requests
import flask_functions
import gRPC_client

app = Flask(__name__)
app.secret_key = "SECRET"

@app.route('/')
def homepage():
    try:
        if session['image_created']:
            img_url = "my_plot.png"
        else:
            img_url = ''
    except KeyError:
        img_url = ''
    session['image_created'] = False
    print('img_url', img_url)
    return render_template('meterusage.html', img_url=img_url)

@app.route('/get-data', methods=['POST'])
def get_data_from_grpc():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        flash('Invalid date range')
        return redirect('/'), 404
    response = gRPC_client.create_gRPC_request(start_date, end_date)
    if not response:
        flash('No data for this time')
        return redirect('/'), 404
    else:
        flask_functions.make_plot(response)
        # session['img_url'] = image_path
        session['image_created'] = True
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    