import requests
import json
import csv

url = "https://api.themoviedb.org/3/certification/movie/list"

# using reuests module to access a website
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTc4YjhlNzNmODVhMzJmNmI0MmNjZjI5YjU5OTg3NCIsInN1YiI6IjY1OWI0ZjBlODc0MWM0MDE0OWQwMjNhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmPACCxVu3VwVZkPj1jogwL0nkH-8V55SIPMaJX1L1k"
}
#  using get() method from requests module to get values from API website 
response = requests.get(url, headers=headers)

# using json.loads() to convert the response json object to python object
cert = json.loads(response.text)

# extracting the countries from the example and storing it in a list
country_list = list (cert['certifications'].keys())
# extrating the list of dictionaries that needs to passed to csv module 
new_cert = (cert['certifications'].values())

# explicitly mentioning the header name or first row name that needs to be in csv file
fieldname = ['country', 'certification','meaning', 'order']

# opening csv file in write mode and assigning field names to it. later using for loop we add the country name to the existing dictionary and inserting the new dicitonary into csv file 
with open('movie_cert.csv', 'w',encoding = "utf-8") as movie_csv :
    csv_writer = csv.DictWriter(movie_csv, fieldnames = fieldname)
    csv_writer.writeheader()
    for key in country_list:
      for value in cert['certifications'][key]:
        value['country'] = key
        csv_writer.writerow(value)

      
      

