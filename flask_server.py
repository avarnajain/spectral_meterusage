from flask import Flask, jsonify, request, render_template, redirect, session
import requests
import flask_functions
import gRPC_client

app = Flask(__name__)
app.secret_key = "SECRET"

@app.route('/')
def homepage():
    try:
        if session['image_created']:
            img_url = "http://my_plot.png"
        else:
            img_url = ''
    except KeyError:
        img_url = ''
    session['image_created'] = False
    return render_template('meterusage.html', img_url=img_url)

@app.route('/get-data')
def get_data_from_grpc():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    response = gRPC_client.create_gRPC_request(start_date, end_date)
    flask_functions.make_plot(response)
    session['image_created'] = True
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    