# from pyspark.sql import SparkSession
# from pyspark.sql.functions import desc
from pyspark.sql import SparkSession
import json
import requests

# import numpy as np
# import pandas as pd

# class Program(Cmd)

#     def do_exit():

#     def do_make_recommendation(self, inp):
#         # Filter dataset for ids of recommended tracks
#         # Sort in descending order number of tags made for songs by artist
#         filtered_table = spark.sql(("SELECT COUNT(tagId), match.track.id " 
#                                     "FROM tag_table "
#                                     "WHERE match.track.metadata.artistName='{0}' "
#                                     "GROUP BY match.track.id "
#                                     "ORDER BY COUNT(tagId) DESC "
#                                     "LIMIT {1}").format(artist, num_recommendations))

#         # Get list of rows
#         rows = filtered_table.collect()
#         recommended_tracks = []
#         for row in rows:
#             recommended_tracks.append(row['id'])

#         return recommended_tracks

if __name__ == "__main__":


    # def retrieve_data():
    #     # create spark session
    #     spark = SparkSession \
    #         .builder \
    #         .appName("TagStream") \
    #         .master("local[2]") \
    #         .getOrCreate()

    #     make_recommendation()

    # TODO: Should fetch this user's tags from api first and store them here
    

    # # make recommendation for popular song from same artist for a tag:
    user_tag = json.loads('{"tagId":"5d34c8b6-99f3-4a7c-9e49-419110ececac","created":"2020-03-23 00:36:34.218 UTC","installationId":"po2lmsfEFcsZIQOuh/FR7GpsC3XLVEJHtJ2TndOAU2yTu8piCxllyHZj6BUESZiFfERjSYOtgFv6XQWIN5k0lA==","geolocation":{"region":{}},"matchCategory":"MUSIC","signatureLength":"12069","match":{"track":{"id":"58929003","adamId":"682704204","metadata":{"artistName":"Rudimental Feat. John Newman","trackTitle":"Feel The Love (Fred V \u0026 Grafix Remix)"},"offset":49.429105468}}}')
    artist = user_tag['match']['track']['metadata']['artistName']

    # # recommend other song by querying tag dump
    # tags = spark.read.json("data/tags.data")

    # tags.tagId.select(*).show()

    # df = pd.read_json(r'data/tags.data', lines=True)
    # df = spark.read.json('data/tags.data')
    # df.registerTempTable('tag_table')

    # def online_make_recommendation(num_recommendations):
        

    # def make_recommendation(num_recommendations):
    #     # Filter dataset for ids of recommended tracks
    #     # Sort in descending order number of tags made for songs by artist
    #     filtered_table = spark.sql(("SELECT COUNT(tagId), match.track.id " 
    #                                 "FROM tag_table "
    #                                 "WHERE match.track.metadata.artistName='{0}' "
    #                                 "GROUP BY match.track.id "
    #                                 "ORDER BY COUNT(tagId) DESC "
    #                                 "LIMIT {1}").format(artist, num_recommendations))

    #     # Get list of rows
    #     rows = filtered_table.collect()
    #     recommended_tracks = []
    #     for row in rows:
    #         recommended_tracks.append(row['id'])

    #     return recommended_tracks

    # print(make_recommendation(num_recommendations=3))
    response = requests.get(('http://localhost:5000/recommend/{0}&{1}').format(artist, 2))
    # print(requests.get(('http://localhost:5000/recommend/{0}?{1}').format(artist, 2)))
    print("Response:", response.text)
    response.close()  # TODO: Is this really needed?
    # print("Code:", response.close)
