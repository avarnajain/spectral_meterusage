from ast import literal_eval
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from flask_server import *

def date_time_to_dict(grpc_response):
    """
    convert grpc string response to dictionary
    with datetime and float values
    """
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
    """
    create a single merged df 
    for all the days the data is requested for
    """
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
    """
    create line plot for the data requested
    return path to plot created
    """
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
    # return image path
    return image_path
