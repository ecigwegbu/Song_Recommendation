from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from flask import Flask
from flask_restful import Resource, Api
import json
import requests
import pycurl
import re  # regex

app = Flask(__name__)
api = Api(app)
apple_api_token = ("eyJraWQiOiI0QTU3OU1DSldSIiwiYWxnIjoiRVMyNTYifQ"
                ".eyJpc3MiOiI0R1dEQkNGNUE0IiwiaWF0IjoxNTg1NjUzM"
                "TYyLCJleHAiOjE1ODYyNTc5NjJ9.km5ZnfszcUipLh-Z3a"
                "aVT47vTevGUxGogg1Gk3fKemnMY6e3rJSdL-T6K8dUkAW7"
                "pN1l_1fChShxL9z6KMfv-Q")

class User(Resource):
    """Process requests for user data."""

    def get(self, user_id, num_recent_tags):
        print("user_id:", user_id)
        print("num_recent_tags:", num_recent_tags)
        user_tag_table = spark.sql(("SELECT * " 
                            "FROM tag_table "
                            "WHERE installationId='{0}' "
                            "ORDER BY created DESC "
                            "LIMIT {1}").format(user_id, num_recent_tags))
        print("JSON:",user_tag_table.toJSON().collect())
        return user_tag_table.toJSON().collect(), 200

class Recommend(Resource):
    """Process song recommendation requests."""

    def get(self, track_id, artist, num_recommendations, recommendation_type):
        # TESTING
        # track_id = '900032829'
        # song_search = requests.get("https://api.music.apple.com/v1/catalog/us/songs/{0}".format(track_id),
        #                             headers={'Authorization': 'Bearer {0}'.format(apple_api_token)})
        # print("contents:", song_search.content)
        # print("headers:", song_search.headers)
        # print("response code:", song_search.status_code)
        # return song_search.json()

        # MORE TESTING
        # track_id = '900032829'
        # print('here')
        # song_json = requests.get("https://api.music.apple.com/v1/catalog/us/songs/{0}".format(track_id),
        #                             headers={'Authorization': 'Bearer {0}'.format(apple_api_token)}).json()
        # song_dict = json.loads(song_json)
        # print("song_json:", song_json)
        # print("\nsong_dict:", song_dict)
        # print('here now')
        # url = song_json['data']['attributes']['url']
        # match = re.search("album/.+?/(.+)\\?")
        # if match:
        #     album_id = match.group(1)
        # print("\n\nalbum_id:\n\n", album_id)
        # return
        print("artist", artist)
        print("num_recommendations", num_recommendations)
        print("recommendation_type", recommendation_type)
        recommended_tracks = self._make_recommendation(track_id, artist, num_recommendations, recommendation_type)
        return recommended_tracks, 200


    def _make_recommendation(self, track_id, artist, num_recommendations, recommendation_type):
        """Make song recommendations for the user."""

        if recommendation_type == 'other_song':
            # Filter tag data for the most Shazamed song titles by the same artist
            filtered_table = spark.sql(("SELECT match.track.metadata.trackTitle " 
                                        "FROM tag_table "
                                        "WHERE match.track.metadata.artistName='{0}' "
                                        "AND match.track.id!='{1}' "
                                        "GROUP BY match.track.metadata.trackTitle "
                                        "ORDER BY COUNT(tagId) DESC "
                                        "LIMIT {2}").format(artist, track_id, num_recommendations))
            print("\nfiltered_table:",filtered_table.collect())

        # EXTENSION: IMPLEMENTATION INCOMPLETE
        # if recommendation_type == 'other_album':
        #     # Need apple API for this
        #     # Filter tag data for Shazams for recently released albums.
        #     track_id = '900032829'
        #     song_json = json.loads(requests.get("https://api.music.apple.com/v1/catalog/us/songs/{0}".format(track_id),
        #                                headers={'Authorization': 'Bearer {0}'.format(apple_api_token)}).json())
        #     url = song_json['data']['attributes']['url']
        #     match = re.search("album/.+?/(.+)\\?")
        #     if match:
        #         album_id = match.group(1)
        #     album_search = json.loads(requests.get("https://api.music.apple.com/v1/catalog/us/songs/{0}".format(track_id),
        #                                headers={'Authorization': 'Bearer {0}'.format(apple_api_token)}).json())
        #     r = requests.get(("https://api.music.apple.com/v1/catalog/us/search?term={0}&limit=1&types=albums").format(album_id),
        #                      headers={'Authorization': ('access_token {0}').format(apple_api_token)})

        return filtered_table.toJSON().collect()

api.add_resource(Recommend, '/recommend/<string:track_id>&<string:artist>&<int:num_recommendations>&<string:recommendation_type>')
api.add_resource(User, '/user/<string:user_id>&<int:num_recent_tags>')

if __name__ == '__main__':

    # Set up spark session for sql query functionality
    spark = SparkSession \
        .builder \
        .appName("TagStream") \
        .master("local[2]") \
        .getOrCreate()
    df = spark.read.json('tag_service/data/tags.data')
    df.registerTempTable('tag_table')

    # Listen on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)