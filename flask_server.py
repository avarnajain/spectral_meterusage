from flask import Flask, jsonify, request, render_template
from datetime import datetime
import flask_functions
import gRPC_client

app = Flask(__name__)
app.secret_key = "SECRET"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
    """
    Route with form to fill in dates
    """
    return render_template('meterusage.html')

@app.route('/get-data', methods=['POST'])
def get_data_from_grpc():
    """
    Route to handle form data
    """
    # get form data
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    # check if form data is valid
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    # return invalid if not
    except ValueError:
        return jsonify({'error': 'Invalid date range'})
    response = gRPC_client.create_gRPC_request(start_date, end_date)
    # if requested data does not exist, return error
    if not response:
        return jsonify({'error': 'No data for this time'})
    # return path to plot
    else:
        image_path = flask_functions.make_plot(response)
        return jsonify({'successful': image_path})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    