import requests
from store import Store

class User:
    """Class to store all relevant information for a user 
    including the tags they have made."""

    def __init__(self, id):
        self.id = id
        self.tags = []

    def get_recommendation(self, tag_id, recommendation_type):
        """Return similar song to track_id that has been a popular tag worldwide.
        :param tag_id: The identifier of the tag the user made. 
        :param recommendation_type: String denoting the metric popularity will be defined on
        """
        # make api request for album that song is in
        
        store = Store()
        album = store.tags[tag_id]match.track.adamid

        spark = SparkSession \
        .builder \
        .appName("TagStream") \
        .master("local[2]") \
        .getOrCreate()

        tags = spark.read.json("data/tags.data")

        tags\
            .select("match.track.id") \
            .groupBy("id") \
            .count() \
            .orderBy(desc("count")) \
            .show(10)

        r = requests.get('https://api.music.apple.com/v1/catalog/{storefront}/search')