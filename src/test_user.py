import unittest
import lame_pigeon_identifier as lpid
from user import *


class TestUser(unittest.TestCase):

    def testUserCreate(self):
        user_id = lpid.LPID(1)
        user_name = "Rzevskiy"

        user = User(user_id, user_name)
        print("Created user:", user)

        self.assertEqual(user.getName(), user_name, msg=("User name is incorrect"))
        self.assertEqual(user.getUserId(), user_id, msg= "User id is incorrect")

    def testChangeUserName(self):
        user_id = lpid.LPID(1)
        user_name = "Rzevskiy"

        user = User(user_id, user_name)
        print("Created user:", user)

        new_name = "Bolkonskiy"
        user.setUserName(new_name)
        print("User with new name:", user)

        self.assertEqual(user.getName(), new_name, msg=("User name is incorrect"))
        self.assertEqual(user.getUserId(), user_id, msg= "User id is incorrect")


class TestUserManager(unittest.TestCase):
    
    def testCreateUser(self):
        um = UserManager()

        user_name = "Vovochka"
        um.createUser(user_name)

        self.assertEqual(um.getUser(LPID(1)).getName(), user_name)
    
    def testIsUserExist(self):
        um = UserManager()

        um.createUser("Vovochka")
        um.createUser("Shtirliz")
        um.createUser("Chapaev")
        print("User Manager: %s" % (um,))

        self.assertTrue(um.isUserExists(LPID(1)))
        self.assertTrue(um.isUserExists(LPID(2)))
        self.assertTrue(um.isUserExists(LPID(3)))
        self.assertFalse(um.isUserExists(LPID(4)))
    

if __name__ == "__main__":
    unittest.main()