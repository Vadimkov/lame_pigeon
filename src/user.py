from lame_pigeon_identifier import LPID
from lame_pigeon_identifier import LPIDManager

class User:

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.setUserName(name)

    def getName(self):
        return self.name

    def getUserId(self):
        return self.user_id

    def setUserName(self, name):
        self.name = name

    def __repr__(self):
        return "User(id=%s, name=%s)" % (self.getUserId(), self.getName())

    def __eq__(self, other):
        return self.getUserId() == other.getUserId()


class UserManager:

    def __init__(self):
        self._users = dict()
        self._lpid_manager = LPIDManager()

    def isUserExists(self, user_id):
        return user_id in self._users

    def getUser(self, user_id):
        return self._users[user_id]

    def createUser(self, user_name):
        new_user = User(self._lpid_manager.next(), user_name)
        self._addUser(new_user)

    def _addUser(self, user):
        self._users[user.getUserId()] = user

    def __repr__(self):
        return "UserManager[%s]" % (len(self._users))

