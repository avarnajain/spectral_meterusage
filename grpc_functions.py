import csv
from datetime import datetime, timedelta

# get meter usage data for between the start and end date
def get_data(date_start, date_end):
    # csv filename
    filename = "meterusage.csv"
    # user specified start date
    start = datetime.strptime(date_start, '%Y-%m-%d')
    # user specified end date
    end = datetime.strptime(date_end, '%Y-%m-%d')
    # add 1 day to end date to make it inclusive
    end += timedelta(days=1, minutes=-15)
    # initialize return dictionary
    usage_dict = {}
    # open csv file
    with open(filename, 'r') as meterusage_file:
        meterusage_reader = csv.reader(meterusage_file)
        # skip header row
        next(meterusage_reader)
        # loop through all rows
        for row in meterusage_reader:
            datetime_obj = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            # if datetime falls within range
            if datetime_obj >= start and datetime_obj <= end:
                date = datetime_obj.date().strftime("%Y-%m-%d")
                time = datetime_obj.time().strftime("%H:%M:%S")
                # add to dictionary
                if date in usage_dict:
                    usage_dict[date].append({'time': time, 'value': row[1]})
                else:
                    usage_dict[date] = [{'time': time, 'value': row[1]}]
    # return dictionary formatted as a string
    return str(usage_dict)