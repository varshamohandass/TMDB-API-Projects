import urllib.parse
import requests
import json
import csv

url = "https://api.themoviedb.org/3/movie/changes?page=1"

start_date = document.getElementById("sd")

end_date = document.getElementById("ed")

def runapi(*args, **kwargs):
    result = Element("Output")
    pyscript.write("Output",start_date)
    pyscript.write("Output",end_date)
# param=dict()
# param['start_date'] = start_date
# param['end_date'] = end_date

# res = urllib.parse.urlencode(param, doseq=True) 
# new_url = url +'&' + res 

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
# }

# response = requests.get(new_url, headers=headers)

# cert = json.loads(response.text)
# url = "https://api.themoviedb.org/3/movie/changes"
# total_pages = cert["total_pages"]
# fieldname = ['page', 'id', 'adult']

# for page in range(1,total_pages+1):
#    param["page"] = page
   
#    res = urllib.parse.urlencode(param, doseq=True) 
#    new_url = url + '?' + res
   
#    response = requests.get(new_url, headers=headers)
#    cert = json.loads(response.text)
#    with open(f'{start_date}_{end_date}.csv', 'a',encoding = "utf-8") as movie_list :
#     csv_writer = csv.DictWriter(movie_list, fieldnames = fieldname)
#     csv_writer.writeheader()
#     for i in cert['results']:
#       i["page"] = page
#       csv_writer.writerow(i)
    