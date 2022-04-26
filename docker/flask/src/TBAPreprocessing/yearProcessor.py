

def grab_event_keys_for_year(years: list) -> list:

    from pymongo import MongoClient

    eventCollection = MongoClient('mongodb://root:password@localhost:27017/?authSource=admin').get_database('aiScouting').get_collection('events')

    # Allocate
    event_keys = []
    tba_read_key = 'vSedKwbovtAcDcYzaAl0QjcYwox4xXxC7r5b4zPpNS3X9BC6khgVlGhR3Fox2tYR'
    format_str = 'https://www.thebluealliance.com/api/v3/events/{year:s}/keys'

    for year in years:

        import requests

        events_for_year = requests.get(url=format_str.format(year=str(year)), headers={'X-TBA-Auth-Key': tba_read_key})

        events_json = events_for_year.json()
        for event in events_json:

            event_keys.append(event)

            event_data = requests.get(url='https://www.thebluealliance.com/api/v3/event/'+event, headers={'X-TBA-Auth-Key': tba_read_key}).json()

            eventCollection.insert_one(event_data)

    return event_keys


if __name__ == "__main__":
    print(grab_event_keys_for_year(['2005', '2006']))

