import csv
from datetime import datetime, timedelta

def get_data(date_str):
    filename = "meterusage.csv"
    date = datetime.strptime(date_str, '%Y-%m-%d')
    usage_list = []
    with open(filename, 'r') as meterusage_file:
        meterusage_reader = csv.reader(meterusage_file)
        next(meterusage_reader)
        for row in meterusage_reader:
            datetime_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            if datetime_obj.date() == date.date():
                usage_list.append(row[1])
    return usage_list
# print(get_data('2019-01-02'))

# def get_data2(start_date, end_date):
#     filename = "meterusage.csv"
#     start = datetime.strptime(start_date, '%Y-%m-%d')
#     end = datetime.strptime(end_date, '%Y-%m-%d')
#     end += timedelta(days=1, minutes=-15)
#     usage_dict = {}
#     with open(filename, 'r') as meterusage_file:
#         meterusage_reader = csv.reader(meterusage_file)
#         next(meterusage_reader)
#         for row in meterusage_reader:
#             datetime_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
#             if datetime_obj >= start and datetime_obj <= end:
#                 usage_dict[datetime_obj] = row[1]
#     return usage_dict