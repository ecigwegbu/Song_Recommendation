from user import User
from tag import Tag

class Store:
    """Record of users and tags."""
    
    self.users = {}  # Map of user_id to User
    self.tags = {}  # Map of tag_id to Tag