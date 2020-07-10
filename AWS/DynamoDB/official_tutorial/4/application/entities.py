class User:

    def __init__(self, item):
        self.username = item.get('username').get('S')
        self.name = item.get('name').get('S')
        self.email = item.get('email').get('S')
        self.birthdate = item.get('birthdate').get('S')
        self.address = item.get('address').get('S')
        self.status = item.get('status').get('S')
        self.interests = item.get('interests').get('S')
        self.pinned_image = item.get('pinnedImage', {}).get('S')
        self.recommended_friends = item.get('recommendedFriends', {}).get('L')

    def __repr__(self):
        return "User<{} -- {}>".format(self.username, self.name)


class Photo:

    def __init__(self, item):
        self.username = item.get('username').get('S')
        self.timestamp = item.get('timestamp').get('S')
        self.location = item.get('location').get('S')

    def __repr__(self):
        return "Photo<{} -- {}>".format(self.username, self.timestamp)

class Reaction:

    def __init__(self, item):
        self.reacting_user = item.get('reactingUser').get('S')
        self.photo = item.get('photo').get('S')
        self.reaction_type = item.get('reactionType').get('S')
        self.timestamp = item.get('timestamp').get('S')

    def __repr__(self):
        return "Reaction<{} -- {} -- {}>".format(self.reacting_user, self.photo, self.reaction_type)

class Friendship:

    def __init__(self, item):
        self.followed_user = item.get('followedUser').get('S')
        self.following_user = item.get('followingUser').get('S')
        self.timestamp = item.get('timestamp').get('S')

    def __repr__(self):
        return "Friendship<{} -- {}>".format(self.followed_user, self.following_user)
