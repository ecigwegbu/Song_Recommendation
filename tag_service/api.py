# TODO: Implement a server that can be queried over a network.
# This server will store Shazam tag data
# Think about how this server will be queried.
# Perhaps make a REST API
# So client (app.py) makes JSON request to API
# Then this server (server.py) makes SQL query for relevant information
# Then server returns result of query to client
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

from flask import Flask
from flask_restful import Resource, Api  # Is this line needed?

import json
# import markdown
import os  # WHY do we import this?

# This is the application factory function
# def create_tag_server():
#     server = Flask(__name__)

# @server.route("/")
# def index():
#     """Present some documentation."""

#     # Open the README file
#     # with open(os.path.dirname(server.route_path) + 'README.md', 'r') as markdown_file"

#         # Read the content of the file
#         # content = markdown_file.read()

#         # Convert to HTML
#         # return markdown.markdown
        
#     content = "Hello world!"

#     Convert to HTML
#     return markdown.markdown

app = Flask(__name__)
api = Api(app)

# class SetUp():
#     def tag_table(self):
#         spark = SparkSession \
#             .builder \
#             .appName("TagStream") \
#             .master("local[2]") \
#             .getOrCreate()
#         df = spark.read.json('data/tags.data')
#         df.registerTempTable('tag_table')
#         return spark
#         # TODO: Should I use global variable here or return df?

class Recommend(Resource):
    # def get(self):
        # return {
        #     'result': 'The API get request is working!'
        # }
        # spark = SparkSession \
        #     .builder \
        #     .appName("TagStream") \
        #     .master("local[2]") \
        #     .getOrCreate()

        # tags = spark.read.json("data/tags.data")

        # tags\
        #     .select("match.track.id") \
        #     .groupBy("id") \
        #     .count() \
        #     .orderBy(desc("count")) \
        #     .show(10)

        # return {
        #     'result': 'The API get request is working!'
        # }
        # f=open("data/single_tag.data", "r")
        # tag = f.read()
        # tag = json.loads(tag)
        # return tag

    def get(self, artist, num_recommendations):
        print("artist", artist)
        print("num_recommendations", num_recommendations)
        # try:
        recommended_tracks = self._make_recommendation(artist, num_recommendations)
        # except Exception:
            # return 404  # Figure out what correct code is
        return recommended_tracks, 200
        # can -ve number be used in sql limit without error?
    
    # def _obtain_data():
    #     # create spark session
    #     spark = SparkSession \
    #         .builder \
    #         .appName("TagStream") \
    #         .master("local[2]") \
    #         .getOrCreate()

    #     df = spark.read.json('data/tags.data')
    #     df.registerTempTable('tag_table')

    def _make_recommendation(self, artist, num_recommendations):
        # Filter dataset for ids of recommended tracks
        # Sort in descending order number of tags made for songs by artist
        filtered_table = spark.sql(("SELECT COUNT(tagId), match.track.id " 
                                    "FROM tag_table "
                                    "WHERE match.track.metadata.artistName='{0}' "
                                    "GROUP BY match.track.id "
                                    "ORDER BY COUNT(tagId) DESC "
                                    "LIMIT {1}").format(artist, num_recommendations))

        # Get list of rows
        rows = filtered_table.collect()
        recommended_tracks = []
        for row in rows:
            recommended_tracks.append(row['id'])

        return recommended_tracks

api.add_resource(Recommend, '/recommend/<string:artist>&<int:num_recommendations>')

if __name__ == '__main__':
    # perform setup first
    # TODO: should this code go into the API thing? Need to learn how to make API
    # spark = SparkSession \
    #     .builder \
    #     .appName("TagStream") \
    #     .master("local[2]") \
    #     .getOrCreate()

    # df = spark.read.json('data/tags.data')
    # df.registerTempTable('tag_table')

    # spark = SetUp().tag_table()
    spark = SparkSession \
        .builder \
        .appName("TagStream") \
        .master("local[2]") \
        .getOrCreate()
    df = spark.read.json('data/tags.data')
    df.registerTempTable('tag_table')

    # run api
    # app.run(host='0.0.0.0', port=80, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)