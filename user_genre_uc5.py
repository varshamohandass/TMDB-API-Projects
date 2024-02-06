import requests
import json
import urllib.parse


user_genre = input("Enter the Genre:")

# Getting list of genres from Genre-Movie API

url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
}

response = requests.get(url, headers=headers)
genre = json.loads(response.text)

genres= genre["genres"]


for genre in genres:
  if genre['name'].lower() == user_genre.lower():
    user_genre_name=genre['name']
    user_genre_id=genre['id']

print(user_genre_name)
print(user_genre_id) 
final_movie_list =[]


url = "https://api.themoviedb.org/3/movie/changes?end_date=2024-01-24&page=1&start_date=2024-01-23"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
}

response = requests.get(url, headers=headers)
movies = json.loads(response.text)

print(movies['results'])

for movie in movies['results']:
  
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

  for j in movie_details['genres']:
    if user_genre_id == j['id']:
      print(movie_details)
      final_movie_list.append(movie_details['title'])
print(final_movie_list)
  