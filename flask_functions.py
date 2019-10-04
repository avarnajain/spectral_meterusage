from ast import literal_eval
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from flask_server import *

response_str = "{'2019-01-01': [{'time': '00:15:00', 'value': '55.09'}, {'time': '00:30:00', 'value': '54.64'}, {'time': '00:45:00', 'value': '55.18'}, {'time': '01:00:00', 'value': '56.03'}, {'time': '01:15:00', 'value': '55.77'}, {'time': '01:30:00', 'value': '55.45'}, {'time': '01:45:00', 'value': '55.74'}, {'time': '02:00:00', 'value': '55.8'}, {'time': '02:15:00', 'value': '55.62'}, {'time': '02:30:00', 'value': '55.45'}, {'time': '02:45:00', 'value': '55.52'}, {'time': '03:00:00', 'value': '56.0'}, {'time': '03:15:00', 'value': '55.88'}, {'time': '03:30:00', 'value': '59.57'}, {'time': '03:45:00', 'value': '62.9'}, {'time': '04:00:00', 'value': '62.54'}, {'time': '04:15:00', 'value': '62.18'}, {'time': '04:30:00', 'value': '62.86'}, {'time': '04:45:00', 'value': '62.73'}, {'time': '05:00:00', 'value': '62.84'}, {'time': '05:15:00', 'value': '63.52'}, {'time': '05:30:00', 'value': '78.1'}, {'time': '05:45:00', 'value': '108.79'}, {'time': '06:00:00', 'value': '111.19'}, {'time': '06:15:00', 'value': '118.67'}, {'time': '06:30:00', 'value': '135.37'}, {'time': '06:45:00', 'value': '142.55'}, {'time': '07:00:00', 'value': '145.97'}, {'time': '07:15:00', 'value': '141.31'}, {'time': '07:30:00', 'value': '133.58'}, {'time': '07:45:00', 'value': '131.19'}, {'time': '08:00:00', 'value': '133.22'}, {'time': '08:15:00', 'value': '135.18'}, {'time': '08:30:00', 'value': '134.71'}, {'time': '08:45:00', 'value': '134.07'}, {'time': '09:00:00', 'value': '134.11'}, {'time': '09:15:00', 'value': '137.63'}, {'time': '09:30:00', 'value': '134.85'}, {'time': '09:45:00', 'value': '137.01'}, {'time': '10:00:00', 'value': '134.23'}, {'time': '10:15:00', 'value': '135.59'}, {'time': '10:30:00', 'value': '136.59'}, {'time': '10:45:00', 'value': '134.23'}, {'time': '11:00:00', 'value': '134.19'}, {'time': '11:15:00', 'value': '137.59'}, {'time': '11:30:00', 'value': '137.03'}, {'time': '11:45:00', 'value': '137.12'}, {'time': '12:00:00', 'value': '135.45'}, {'time': '12:15:00', 'value': '132.78'}, {'time': '12:30:00', 'value': '134.73'}, {'time': '12:45:00', 'value': '135.4'}, {'time': '13:00:00', 'value': '135.3'}, {'time': '13:15:00', 'value': '132.93'}, {'time': '13:30:00', 'value': '133.68'}, {'time': '13:45:00', 'value': '135.07'}, {'time': '14:00:00', 'value': '132.15'}, {'time': '14:15:00', 'value': '131.06'}, {'time': '14:30:00', 'value': '134.0'}, {'time': '14:45:00', 'value': '132.56'}, {'time': '15:00:00', 'value': '131.19'}, {'time': '15:15:00', 'value': '130.33'}, {'time': '15:30:00', 'value': '130.77'}, {'time': '15:45:00', 'value': '131.64'}, {'time': '16:00:00', 'value': '135.8'}, {'time': '16:15:00', 'value': '134.58'}, {'time': '16:30:00', 'value': '131.9'}, {'time': '16:45:00', 'value': '130.41'}, {'time': '17:00:00', 'value': '133.33'}, {'time': '17:15:00', 'value': '138.18'}, {'time': '17:30:00', 'value': '129.98'}, {'time': '17:45:00', 'value': '116.3'}, {'time': '18:00:00', 'value': '108.53'}, {'time': '18:15:00', 'value': '107.82'}, {'time': '18:30:00', 'value': '107.84'}, {'time': '18:45:00', 'value': '106.18'}, {'time': '19:00:00', 'value': '106.75'}, {'time': '19:15:00', 'value': '108.4'}, {'time': '19:30:00', 'value': '105.72'}, {'time': '19:45:00', 'value': '105.95'}, {'time': '20:00:00', 'value': '93.74'}, {'time': '20:15:00', 'value': '87.41'}, {'time': '20:30:00', 'value': '87.36'}, {'time': '20:45:00', 'value': '94.94'}, {'time': '21:00:00', 'value': '132.83'}, {'time': '21:15:00', 'value': '110.53'}, {'time': '21:30:00', 'value': '84.24'}, {'time': '21:45:00', 'value': '80.86'}, {'time': '22:00:00', 'value': '70.35'}, {'time': '22:15:00', 'value': '59.63'}, {'time': '22:30:00', 'value': '55.18'}, {'time': '22:45:00', 'value': '54.47'}, {'time': '23:00:00', 'value': '55.08'}, {'time': '23:15:00', 'value': '55.11'}, {'time': '23:30:00', 'value': '55.19'}, {'time': '23:45:00', 'value': '55.56'}], '2019-01-02': [{'time': '00:00:00', 'value': '55.87'}, {'time': '00:15:00', 'value': '55.67'}, {'time': '00:30:00', 'value': '55.43'}, {'time': '00:45:00', 'value': '56.03'}, {'time': '01:00:00', 'value': '56.63'}, {'time': '01:15:00', 'value': '57.51'}, {'time': '01:30:00', 'value': '57.68'}, {'time': '01:45:00', 'value': '57.91'}, {'time': '02:00:00', 'value': '57.71'}, {'time': '02:15:00', 'value': '58.32'}, {'time': '02:30:00', 'value': '58.37'}, {'time': '02:45:00', 'value': '58.27'}, {'time': '03:00:00', 'value': '58.68'}, {'time': '03:15:00', 'value': '58.2'}, {'time': '03:30:00', 'value': '63.06'}, {'time': '03:45:00', 'value': '67.94'}, {'time': '04:00:00', 'value': '68.69'}, {'time': '04:15:00', 'value': '67.62'}, {'time': '04:30:00', 'value': '67.4'}, {'time': '04:45:00', 'value': '68.45'}, {'time': '05:00:00', 'value': '73.29'}, {'time': '05:15:00', 'value': '78.36'}, {'time': '05:30:00', 'value': '102.68'}, {'time': '05:45:00', 'value': '162.75'}, {'time': '06:00:00', 'value': '164.7'}, {'time': '06:15:00', 'value': '151.26'}, {'time': '06:30:00', 'value': '156.94'}, {'time': '06:45:00', 'value': '173.5'}, {'time': '07:00:00', 'value': '180.35'}, {'time': '07:15:00', 'value': '182.95'}, {'time': '07:30:00', 'value': '199.31'}, {'time': '07:45:00', 'value': '221.18'}, {'time': '08:00:00', 'value': '233.64'}, {'time': '08:15:00', 'value': '239.33'}, {'time': '08:30:00', 'value': '252.93'}, {'time': '08:45:00', 'value': '260.4'}, {'time': '09:00:00', 'value': '262.83'}, {'time': '09:15:00', 'value': '261.67'}, {'time': '09:30:00', 'value': '263.98'}, {'time': '09:45:00', 'value': '263.55'}, {'time': '10:00:00', 'value': '261.75'}, {'time': '10:15:00', 'value': '269.27'}, {'time': '10:30:00', 'value': '270.87'}, {'time': '10:45:00', 'value': '268.86'}, {'time': '11:00:00', 'value': '264.86'}, {'time': '11:15:00', 'value': '261.57'}, {'time': '11:30:00', 'value': '259.88'}, {'time': '11:45:00', 'value': '254.46'}, {'time': '12:00:00', 'value': '259.45'}, {'time': '12:15:00', 'value': '262.77'}, {'time': '12:30:00', 'value': '258.37'}, {'time': '12:45:00', 'value': '260.17'}, {'time': '13:00:00', 'value': '258.99'}, {'time': '13:15:00', 'value': '255.46'}, {'time': '13:30:00', 'value': '253.93'}, {'time': '13:45:00', 'value': '252.2'}, {'time': '14:00:00', 'value': '246.99'}, {'time': '14:15:00', 'value': '247.32'}, {'time': '14:30:00', 'value': '248.06'}, {'time': '14:45:00', 'value': '243.94'}, {'time': '15:00:00', 'value': '245.46'}, {'time': '15:15:00', 'value': '246.22'}, {'time': '15:30:00', 'value': '241.72'}, {'time': '15:45:00', 'value': '239.55'}, {'time': '16:00:00', 'value': '240.96'}, {'time': '16:15:00', 'value': '238.41'}, {'time': '16:30:00', 'value': '228.85'}, {'time': '16:45:00', 'value': '227.15'}, {'time': '17:00:00', 'value': '232.01'}, {'time': '17:15:00', 'value': '227.23'}, {'time': '17:30:00', 'value': '206.15'}, {'time': '17:45:00', 'value': '179.32'}, {'time': '18:00:00', 'value': '155.34'}, {'time': '18:15:00', 'value': '138.3'}, {'time': '18:30:00', 'value': '131.47'}, {'time': '18:45:00', 'value': '136.15'}, {'time': '19:00:00', 'value': '178.71'}, {'time': '19:15:00', 'value': '161.46'}, {'time': '19:30:00', 'value': '133.63'}, {'time': '19:45:00', 'value': '126.96'}, {'time': '20:00:00', 'value': '123.07'}, {'time': '20:15:00', 'value': '121.82'}, {'time': '20:30:00', 'value': '144.74'}, {'time': '20:45:00', 'value': '164.83'}, {'time': '21:00:00', 'value': '133.33'}, {'time': '21:15:00', 'value': '114.83'}, {'time': '21:30:00', 'value': '114.96'}, {'time': '21:45:00', 'value': '104.22'}, {'time': '22:00:00', 'value': '73.33'}, {'time': '22:15:00', 'value': '54.19'}, {'time': '22:30:00', 'value': '50.14'}, {'time': '22:45:00', 'value': '49.76'}, {'time': '23:00:00', 'value': '49.61'}, {'time': '23:15:00', 'value': '47.23'}, {'time': '23:30:00', 'value': '46.0'}, {'time': '23:45:00', 'value': '45.97'}]}"

def date_time_to_dict(grpc_response):
    """convert grpc string response to dictionary
    with datetime keys and float values"""
    grpc_response_dict = literal_eval(grpc_response)
    meter_usage_dict = {}
    for date, times in grpc_response_dict.items():
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        meter_usage_dict[date_obj] = []
        for item in grpc_response_dict[date]:
            time_obj = datetime.strptime(item['time'], '%H:%M:%S').time()
            meter_value = float(item['value'])
            meter_usage_dict[date_obj].append({'time': time_obj, date: meter_value})
    return meter_usage_dict

def create_df(response_str):
    # get datetime dict from grpc string
    data = date_time_to_dict(response_str)
    # initialize empty list
    dfs = []
    # boolean to start merging
    can_merge = False
    # for each day in our dictionary
    for key in data.keys():
        # create df
        df = pd.DataFrame(data[key])
        # append df
        dfs.append(df)
        # if can_merge is true
        if can_merge:
            df1 = dfs[0]
            df2 = dfs[1]
            # merge dfs
            df = pd.merge(df1, df2, on='time', how='outer', sort=True)
            # reset dfs to merged df
            dfs = [df]
        # set can_merge to true after first df has been added
        can_merge = True
    # return merged df
    return dfs[0]

def make_plot(response_str):
    # get merged dataframe
    df = create_df(response_str)
    # create plot
    fig, ax = plt.subplots()
    df.plot(x='time', ax=ax, legend=True)
    ax.set_title("Meter Usage Over Time")
    ax.xaxis.set_ticks(['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'])
    ax.xaxis.set_label_text("Hour of the Day")
    ax.yaxis.set_label_text("Meter Usage")
    # save plot
    image_path = "{}.png".format(datetime.now().time())
    fig.savefig('static/{}'.format(image_path))
    return image_path
