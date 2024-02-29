import requests
import json
import urllib.parse
import csv
import pandas as pd
from dotenv import load_dotenv
import os


# Getting list of genres from Genre-Movie API
load_dotenv(".env")
url = os.getenv("genre_api")
apikey = os.getenv("apikey")
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {apikey}"
}

response = requests.get(url, headers=headers)
genre = json.loads(response.text)

genres= genre["genres"]
new_fieldname=['genre_name','genre_id','movie_name','thumbnail']

for genre in genres:
  genre_name=genre['name']
  genre_id=genre['id']
  with open(f'{genre_name}_{genre_id}.csv', 'w',encoding = "utf-8") as genre_file :
          csv_writer = csv.DictWriter(genre_file, fieldnames = new_fieldname)
          csv_writer.writeheader()

add_movie = {}
final_movie_list=[]
movielist=[]


# Getting start date and end date from user appending it to MovieList url

url = os.getenv("movie_chng_api1")


start_date = input("Enter start date in YYYY-MM-DD format: ")
end_date = input("Enter end date in YYYY-MM-DD format: ")

param=dict()
param['start_date'] = start_date
param['end_date'] = end_date

res = urllib.parse.urlencode(param, doseq=True)
new_url = url +'&' + res 


response = requests.get(new_url, headers=headers)

# print(response.text)
cert = json.loads(response.text)

# Movie list API call to receive data in all pages for given start and end date
url = os.getenv("movie_chng_api2")

total_pages = cert["total_pages"]
fieldname = ['page', 'id', 'adult']
movielist = []

for page in range(1,total_pages+1):
  param["page"] = page
  
  res = urllib.parse.urlencode(param, doseq=True)
  new_url = url + '?' + res
  response = requests.get(new_url, headers=headers)
  cert = json.loads(response.text)
  # print(cert)
  with open(f'{start_date}_{end_date}.csv', 'a',encoding = "utf-8") as movie_list :
    csv_writer = csv.DictWriter(movie_list, fieldnames = fieldname, lineterminator='\n')
    csv_writer.writeheader()
    for i in cert['results']:
      if i["adult"] != None:
        i["page"] = page
        csv_writer.writerow(i)
        movielist.append(i['id'])
print(movielist, len(movielist))


# calling movie details api for each movie present in movie list api.
for movie in movielist:
  movie_details_url = os.getenv("movie_details_api")
  movie_url = movie_details_url.format(movie = movie)
  

  response = requests.get(movie_url, headers=headers)
  movie_details = json.loads(response.text)
  # print(movie_details)

  # print(movie_details['original_title'])

  # comparing genre present in movie details to the genre present in genres result and add the movie with its details to respectvie genre file
  if 'genres' in movie_details:     
    for i in genres:
      for j in movie_details['genres']:
        if i['name'] == j['name']:
          add_movie['genre_name'] = i['name']
          add_movie['genre_id'] = i['id']
          add_movie['movie_name'] = movie_details['title']
          add_movie['thumbnail'] = movie_details['poster_path']
          final_movie_list.append(add_movie)
          # print(add_movie)
          genre_name = add_movie['genre_name']
          genre_id= add_movie['genre_id']
          with open(f'{genre_name}_{genre_id}.csv', 'a',encoding = "utf-8") as genre_file :
            csv_writer = csv.DictWriter(genre_file, fieldnames = new_fieldname, lineterminator='\n')
            # csv_writer.writeheader()
            csv_writer.writerow(add_movie)
  else:
    continue

for genre in genres:
  genre_name=genre['name']
  genre_id=genre['id']   
  aa = pd.read_csv(f'{genre_name}_{genre_id}.csv')  
  total_rows = len(aa)
  aa.to_csv(f'{genre_name}_{genre_id}_{total_rows}.csv', index_label='index') 

print(f'completed making changes to {genre_name}_{genre_id}.csv')
print('finished making changes to all files')
print("finished creating file")


