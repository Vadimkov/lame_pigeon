from lame_pigeon_identifier import LPID
from lame_pigeon_identifier import LPIDManager


class Chat:

    def __init__(self, chat_id, users, chat_manager):
        self._chat_id = chat_id
        self._messages = list()

        self._users = dict()
        for user in users:
            self._addUser(user)

        self._cm = chat_manager

    def addUser(self, user):
        self._addUser(user)

    def _addUser(self, user):
        self._users[user.getUserId()] = user

    def pushMessage(self, mes):
        self._messages.append(mes)

        self._cm.pushMessageToChat(mes, self)

    def getChatId(self):
        return self._chat_id

    def getAllUsers(self):
        return self._users.values()


class ChatManager:

    def __init__(self, client_factory):
        self._chats = dict()
        self._lpid_manager = LPIDManager()
        self._client_factory = client_factory

    def isChatExist(self, chat):
        return chat.getChatId() in self._chats

    def createChat(self, creator_user, users):
        new_chat_id = self._lpid_manager.next()
        new_chat = Chat(new_chat_id, users, self)

        self._chats[new_chat_id] = new_chat

    def getChat(self, chat_id):
        return self._chats[chat_id]

    def getAllChatsForUser(self, user_id):
        pass

    def pushMessageToChat(self, message, chat):
        for user in chat.getAllUsers():
            self._client_factory.sendMessage(message, user)
