import requests
import json
import urllib.parse
import csv

# Getting list of genres from Genre-Movie API

url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
}

response = requests.get(url, headers=headers)
genre = json.loads(response.text)

genres= genre["genres"]
new_fieldname=['genre_name','genre_id','movie_name','thumbnail']

# creating a csv file for each genre present

for genre in genres:
  genre_name=genre['name']
  genre_id=genre['id']
  with open(f'{genre_name}_{genre_id}.csv', 'a',encoding = "utf-8") as genre_file :
          csv_writer = csv.DictWriter(genre_file, fieldnames = new_fieldname)
          csv_writer.writeheader()
# print(genres)

add_movie = {}
final_movie_list=[]


# Getting start date and end date from user appending it to MovieList url

url = "https://api.themoviedb.org/3/movie/changes?page=1"

start_date = input("Enter start date in YYYY-MM-DD format: ")
end_date = input("Enter start date in YYYY-MM-DD format: ")

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

# Movie list API call to receive data in all pages for given start and end date
url = "https://api.themoviedb.org/3/movie/changes"
total_pages = cert["total_pages"]
fieldname = ['page', 'id', 'adult']
movielist = []

for page in range(1,total_pages+1):
  param["page"] = page
  
  res = urllib.parse.urlencode(param, doseq=True)
  new_url = url + '?' + res
  headers = {
  "accept": "application/json",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
}
  response = requests.get(new_url, headers=headers)
  cert = json.loads(response.text)
#  print(cert)
  with open(f'{start_date}_{end_date}.csv', 'a',encoding = "utf-8") as movie_list :
    csv_writer = csv.DictWriter(movie_list, fieldnames = fieldname)
    csv_writer.writeheader()
    for i in cert['results']:
      i["page"] = page
      csv_writer.writerow(i)
for i in cert['results']:
  movielist.append(i)
# print(movielist)


# calling movie details api for each movie present in movie list api.
for movie in movielist:
  movie_id =movie['id']
  
  movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'

  headers = {
  "accept": "application/json",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
  }
  response = requests.get(movie_url, headers=headers)
  movie_details = json.loads(response.text)
  # print(movie_details)
  # print(movie_details['genres'])
  # print(movie_details['original_title'])

  # comparing genre present in movie details to the genre present in genres result and add the movie with its details to respectvie genre file
  for i in genres:
    for j in movie_details['genres']:
      if i['name'] == j['name']:
        add_movie['genre_name'] = i['name']
        add_movie['genre_id'] = i['id']
        add_movie['movie_name'] = movie_details['title']
        add_movie['thumbnail'] = movie_details['poster_path']
        final_movie_list.append(add_movie)
        print(add_movie)
        genre_name = add_movie['genre_name']
        genre_id= add_movie['genre_id']
        with open(f'{genre_name}_{genre_id}.csv', 'a',encoding = "utf-8") as genre_file :
          csv_writer = csv.DictWriter(genre_file, fieldnames = new_fieldname)
          # csv_writer.writeheader()
          csv_writer.writerow(add_movie)



        





      


