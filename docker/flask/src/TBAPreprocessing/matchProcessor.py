from pymongo import MongoClient


def grab_matches_for_events(event_ids: list ):

    def grabMatches(event_id: str, bucket):

        # Allocate strings
        tba_read_key = 'vSedKwbovtAcDcYzaAl0QjcYwox4xXxC7r5b4zPpNS3X9BC6khgVlGhR3Fox2tYR'
        format_str = f'https://www.thebluealliance.com/api/v3/event/{event_id}/matches'

        import requests

        matches_in_event = requests.get(url=format_str, headers={'X-TBA-Auth-Key': tba_read_key})

        matches_json = matches_in_event.json()

        for match in matches_json:
            bucket.insert_one(match)

    matchCollection = MongoClient('mongodb://root:password@localhost:27017/?authSource=admin').get_database('aiScouting').get_collection('matches')

    while len(event_ids) > 0:

        events_to_retry = []

        for individual_event_id in event_ids:
            grabMatches(individual_event_id, matchCollection)

        event_ids = events_to_retry



if __name__ == "__main__":
    grab_matches_for_events(['2019zhrcc'])
