import urllib.parse
from datetime import datetime

import requests
import json
import csv

url = "https://api.themoviedb.org/3/movie/changes?page=1"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
# }

# response = requests.get(url, headers=headers)

# print(response.text)



start_date = input("Enter start date in YYYY-MM-DD format: ")
end_date = input("Enter start date in YYYY-MM-DD format: ")

# strtdt_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
# enddt_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
# print(strtdt_obj)
# print(enddt_obj)  # printed in default format

param=dict()
param['start_date'] = start_date
param['end_date'] = end_date

res = urllib.parse.urlencode(param, doseq=True)
new_url = url +'&' + res

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
}

response = requests.get(new_url, headers=headers)

# print(response.text)
cert = json.loads(response.text)

fieldname = ['id', 'adult']
with open('movie_list.csv', 'w',encoding = "utf-8") as movie_list :
    csv_writer = csv.DictWriter(movie_list, fieldnames = fieldname)
    csv_writer.writeheader()
    for i in cert['results']:
      csv_writer.writerow(i)
    