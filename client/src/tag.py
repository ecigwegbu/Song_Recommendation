class Tag:
    """A class to hold tag objects."""

    def __init__(self, json_string):
        """Initialise Tag object from JSON-style string"""
            self.tag_dict = json.loads(json_string)

    def __getitem__(self, attribute):
        return self.tag_dict[attribute]