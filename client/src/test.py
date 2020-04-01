# from pyspark.sql import SparkSession
# from pyspark.sql.functions import desc
from pyspark.sql import SparkSession
import json
import requests


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

    spark = SparkSession \
        .builder \
        .appName("TagStream") \
        .master("local[2]") \
        .getOrCreate()
    df = spark.read.json('data/tags.data')
    df.registerTempTable('tag_table')

    user_id = "po2lmsfEFcsZIQOuh/FR7GpsC3XLVEJHtJ2TndOAU2yTu8piCxllyHZj6BUESZiFfERjSYOtgFv6XQWIN5k0lA=="

    timestamps = spark.sql(("SELECT created " 
                                "FROM tag_table "
                                "ORDER BY created DESC").format(user_id))
    print("timestamps:", timestamps.collect())

    print("DataFrame:", len(df.collect()))
    # Get tags made by user
    num_most_recent_tags = 5
    user_tag_table = spark.sql(("SELECT * " 
                                "FROM tag_table "
                                "WHERE installationId='{0}' "
                                "ORDER BY created DESC "
                                "LIMIT {1}").format(user_id, num_most_recent_tags))

    print("user tag table:", len(user_tag_table.collect()))
    # TODO: Should fetch this user's tags from api first and store them here
    # Or perhaps not. The purpose of this app could be to make a recommendation for the user right after he Shazams
    # So the tag used in this file assumes this is the Shazam the user made

    # # make recommendation for popular song from same artist for a tag:
    user_tag = json.loads('{"tagId":"5d34c8b6-99f3-4a7c-9e49-419110ececac","created":"2020-03-23 00:36:34.218 UTC","installationId":"po2lmsfEFcsZIQOuh/FR7GpsC3XLVEJHtJ2TndOAU2yTu8piCxllyHZj6BUESZiFfERjSYOtgFv6XQWIN5k0lA==","geolocation":{"region":{}},"matchCategory":"MUSIC","signatureLength":"12069","match":{"track":{"id":"58929003","adamId":"682704204","metadata":{"artistName":"Rudimental Feat. John Newman","trackTitle":"Feel The Love (Fred V \u0026 Grafix Remix)"},"offset":49.429105468}}}')
    artist = user_tag['match']['track']['metadata']['artistName']

    response = requests.get(('http://localhost:5000/recommend/{0}&{1}').format(artist, 2))
    print("Response:", response.text)
    response.close()
