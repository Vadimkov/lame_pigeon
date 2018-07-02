import unittest
from chat import *
from user import *
from unittest.mock import MagicMock


class TestChat(unittest.TestCase):

    def setUp(self):
        # All objects of ChatManager and ClientFactory should be MagickMock objects
        self._client_factory = MagicMock()
        self.cm = ChatManager(self._client_factory)
        self.user_bob = User(1, "Bob")
        self.user_jim = User(2, "Jim")
        self.users = [self.user_bob, self.user_jim]

    def testCreateChat(self):
        test_chat = Chat(1, self.users, self.cm)
        print(test_chat)

    def testGetAllUsers(self):
        test_chat = Chat(1, self.users, self.cm)
        users_list_from_chat = test_chat.getAllUsers()
        self.assertCountEqual(users_list_from_chat, self.users, "Extra users has been added")
        
    def testGetChatId(self):
        test_chat = Chat(1, self.users, self.cm)
        self.assertEqual(test_chat.getChatId(), 1)

    def testAddUserToChat(self):
        test_chat = Chat(1, self.users, self.cm)
        user_kate = User(14, "Kate")
        test_chat.addUser(user_kate)

        self.users.append(user_kate)

        self.assertCountEqual(test_chat.getAllUsers(), self.users)

    def testPushMessageToChat(self):
        pass


if __name__ == "__main__":
    unittest.main()