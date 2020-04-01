from pyspark.sql import SparkSession

# The goal of this app is to find out what others are 'Shazaming' that you might like - this tells you what songs other people are discovering.
# It is a metric of song discovery popularity
# You should sign in as a user
# The database of tags should be online
# Then, you, the user of the app asks for a recommendation and you specify the type of recommendation you are looking for
#       songs from same album, songs from the same genre, songs that the same artist featured in
#       Remember that these are not just songs pulled out of the Apple catalogue. They are songs that are currenlty being popularly 'Shazamed'

class App:
    """Program starts here."""

    # TODO: Sam had the idea of using a ranking-style system from 4F13 to get the most popular songs. Consider this idea.
    # TODO: I've decided this app should belong to a single user, so tags should not be stored locally. Perhaps I should
    # implement a server that acts as the store for the tags and the user. This app is the client.
    # TODO: Do I need to implement a clean and shiny front-end or should I make this a command-line application? wxPython desktop GUI? How about a web frontend on a browser?
    # NOTE: I should make this app really good so that I can add it to my portfolio. Kill two birds with one stone.
    def __init__(self):
        # tags = {}
        # users = {}

    # def add_user(self, user_id):
    #     """Add user to the record."""

    # def add_tag(self, tag_id):
    #     """Add tag to the record."""

    def make_recommendation(self, user_id, type):
        """
        Recommend a song to user given by user_id.
        :param user_id: String identifier of the user
        :param type: String representing type of recommendation to make
        """