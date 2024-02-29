import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import bson

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

#reading the number of databases 
client = MongoClient(MONGODB_URI)

for db_info in client.list_database_names():
   print(db_info)

# reading the number of collection(tables) in a particular database

db = client['sample_mflix']
collections = db.list_collection_names()

for collection in collections:
   print(collection)

# reading a particular document(Row/record) present in a collection using its title
movies = db['movies']
pprint(movies.find_one({'title':'The Red Head'}))

# inserting a new document to a collection
insert_result = movies.insert_one({'awards': {'nominations': 2, 'text': '1 win.', 'wins': 1},
 'cast': ['Harry Baur', 'Robert Lynen', 'Louis Gauthier', 'Simone Aubry'],
 'countries': ['Germany'],
 'directors': ['Julien Duvivier'],
 'genres': ['Drama'],
 'imdb': {'id': 23387, 'rating': 8.4, 'votes': 252},
 'languages': ['German'],
 'released': datetime.datetime(1934, 5, 18, 0, 0),
 'runtime': 98,
 'title': 'The Green House',})
# printing the id of inserted document
parasite_id = insert_result.inserted_id
print(parasite_id)
# printing the document using it's title
# pprint(movies.find_one({'title':'The Green House'}))
# pprint(movies.find_one({'_id': bson.ObjectId(parasite_id)}))

# for doc in movies.find({'title':'The Green House'}):
#    pprint(doc)

# Updating Documents

update_result=movies.update_many({'title':'The Green House'}, {'$set':{'runtime':105}})
# for doc in movies.find({'title':'The Green House'}):
#    pprint(doc)


# deleting one document
movies.delete_one(
   {"title": "The Green House",}
)

# deleting all movies with title the green house

movies.delete_many(
   {"title": "The Green House",}
)

for doc in movies.find({'title':'The Green House'}):
   pprint(doc)



