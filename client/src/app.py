from pyspark.sql import SparkSession
import json
import requests
from cmd import Cmd
from random import seed
from random import randint
import os
from error_messages import Error, Notice

class Program(Cmd):

    def __init__(self):
        # TODO: Resolve forward-slash escape issue
        self.user_id = "P0xE3q64kMjojjb4UuIlLJqSupFl431XIjoYZrmX7Sd4F4oh29hDDVw0iuAN5uEhrOcNFJg9Z0mBj8UAlWd2Tw=="
        seed()  # seed the random number generator with the system time
        self.user_tag_data = None
        super().__init__()

    def do_exit(self, inp):
        """Exit the program."""
        print("Bye")
        return True

    def do_get_recent_Shazams(self, inp):
        """Download your recent Shazams
        Use format: get_recent_Shazams <num_Shazams>"""

        # num_most_recent_tags = 5
        inp_list = inp.split(" ")
        if len(inp_list) != 1:
            print(Error.invalid_tag_fetch)
            return

        try:
            num_recent_tags = inp.split(" ")[0]
            if not float(num_recent_tags).is_integer():
                print(Error.invalid_num_tags)
                return
            elif int(num_recent_tags) < 0:
                print(Error.invalid_num_tags)
                return
            else:

                # TODO: EXTENSION: Change this such that you add more to user tag data rather than changing it
                self.user_tag_data = requests.get(('http://localhost:5000/user/{0}&{1}').format(self.user_id, num_recent_tags)).json()
                print(self.user_tag_data)
        except Exception:
            print(Error.invalid_tag_fetch)
            return


    def do_make_recommendation(self, inp):
        """Get recommendation for song based on your Shazams.
        Use Format: make_recommendation <other_song|other_album> <num_recommendations>
        Note: The other_album is an extension feature that has not yet been fully implemented."""

        if self.user_tag_data is None:
            print(Notice.no_user_tags)
            return

        rand_tag = self._rand_user_tag()
        artist = rand_tag['match']['track']['metadata']['artistName']
        track_id = rand_tag['match']['track']['id']

        try:
            (recommendation_type, num_recommendations) = inp.split(" ")
        except Exception:
            print(Error.recommendation_syntax)
            return

        try:
            if not (recommendation_type=='other_song'): # TODO: EXTENSION ... or recommendation_type=='other_album'):
                print(Error.unrecognised_recommendation)
                return
            if not float(num_recommendations).is_integer():
                print(Error.invalid_num_recommendations)
                return
            elif int(num_recommendations) < 0:
                print(Error.invalid_num_recommendations)
                return
            else:
                recommended_tags = requests.get(('http://localhost:5000/recommend/{0}&{1}&{2}&{3}').format(track_id, artist, num_recommendations, recommendation_type)).json()
                print("\nSongs recommended just for you:")
                for tag in recommended_tags:
                    print(json.loads(tag)['trackTitle'])  # Should there be a newline here?
        except Exception:
            print(Error.recommendation_syntax)
            return

    def _rand_user_tag(self):
        num_tags = len(self.user_tag_data)
        tags = self.user_tag_data
        return json.loads(self.user_tag_data[randint(0,num_tags-1)])

    # EXTENSION: Implementation not complete
    # def do_recommendation_history(self, inp):
    #     """Show the user a history of the recommendations they were made.
    #     Use the format: recommendation_history"""
    #     # TODO
    #     # If item already in recommendation history then be sure not to add it again
    #     pass


if __name__ == "__main__":

    Program().cmdloop()
