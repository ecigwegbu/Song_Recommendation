class Error:
    """Error messages for invalid user input."""

    invalid_command = ("\nCommand not recognised.\n"
                       "Enter '?' or 'help' for more information.\n")

    recommendation_syntax = ("\nYou have not entered the command in the correct format.\n"
                             "Get a recommendation using the format:\n"
                             "make_recommendation <other_song|other_album> <num_recommendations>\n"
                             "Enter '?' or 'help' for more information.\n")

    unrecognised_recommendation = ("\nThat recommendation type is not recognised.\n"
                                   "The options currently available are: other_song\n"
                                   "Enter '?' or 'help' for more information.\n")

    invalid_num_recommendations = ("Invalid number of recommendations.\n"
                                   "It must be a non-negative integer.")

    invalid_tag_fetch = ("\nYou have not entered the command in the correct format.\n"
                         "Download your recent Shazams using the format:\n"
                         "get_recent_tags <num_Shazams>\n"
                         "Enter '?' or 'help' for more information.\n")
    
    invalid_num_tags = ("Invalid number of Shazams.\n"
                        "It must be a non-negative integer.")

class Notice:
    """Notifications for the user."""

    no_user_tags = ("\nThere is no Shazam data available to make a personalised song recommendation.\n"
                    "Download your most recent Shazam history using the command: get_recent_tags\n"
                    "Enter '?' or 'help' for more information.\n")
