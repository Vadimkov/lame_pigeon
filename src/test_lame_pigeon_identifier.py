import unittest
from lame_pigeon_identifier import *

class TestLPID(unittest.TestCase):

    def testAddAndEqual(self):
        lpid1 = LPID(1)
        lpid2 = LPID(2)
        print("LPID:", lpid1)
        
        self.assertEqual(lpid1 + 1, lpid2)
        self.assertEqual(lpid1 + 0, lpid1)
        self.assertNotEqual(lpid1 + 1, lpid1)


class TestLPIDManager(unittest.TestCase):

    def testNext(self):
        manager = LPIDManager()
        print("LPIDManager:", manager)

        lpid_list = list()
        for i in range(5000):
            lpid = manager.next()
            self.assertFalse(lpid in lpid_list)
            lpid_list.append(lpid)


if __name__ == "__main__":
    unittest.main()