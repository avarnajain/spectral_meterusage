import csv
from datetime import datetime, timedelta

filename = "meterusage.csv"

def get_data(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    end += timedelta(days=1, minutes=-15)
    usage_dict = {}
    with open(filename, 'r') as meterusage_file:
        meterusage_reader = csv.reader(meterusage_file)
        next(meterusage_reader)
        for row in meterusage_reader:
            datetime_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            if datetime_obj >= start and datetime_obj <= end:
                usage_dict[datetime_obj] = row[1]
    return usage_dict
# print(get_data('2019-01-01', '2019-01-03'))