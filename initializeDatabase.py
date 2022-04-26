import time

from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from datetime import date
from docker.flask.src.TBAPreprocessing.yearProcessor import grab_event_keys_for_year
from docker.flask.src.TBAPreprocessing.matchProcessor import grab_matches_for_events
time.sleep(5)

client = MongoClient('mongodb://root:password@localhost:27017/?authSource=admin')
db = client['aiScouting']

try:
    db.create_collection('matches')
except CollectionInvalid:
    print("Collection 'matches' already exists")

try:
    db.create_collection('events')
except CollectionInvalid:
    print("Collection 'events' already exists")

try:
    db.create_collection('robots')
except CollectionInvalid:
    print("Collection 'robots' already exists")

current_year = date.today().year

years = []

for i in range(-1, 1):
    years.append(current_year + i)

event_keys = grab_event_keys_for_year(years)
grab_matches_for_events(event_keys)


