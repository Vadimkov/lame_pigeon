import unittest
import message

message1xml = """<?xml version="1.0" ?>
<message type="CHAT">
    <destination chat_id="ChatId"/>
    <send_time>26521758127878</send_time>
    <receive_time>527625371587</receive_time>
    <sender_user>UserId</sender_user>
    <body>It is my message</body>
</message>"""

class TestChatMessage(unittest.TestCase):
    """Unittests for ChatMessage and parsing/serialisation chzt-messages"""

    def setUp(self):
        message1xml = """<?xml version="1.0" ?>
<message type="CHAT">
    <destination chat_id="ChatId"/>
    <send_time>26521758127878</send_time>
    <receive_time>527625371587</receive_time>
    <sender_user>UserId</sender_user>
    <body>It is my message</body>
</message>"""

        self.message1 = message.parseMessage(message1xml)
    
    def testTypeMessage(self):
        self.assertEqual(message.MessageType.CHAT, self.message1.getType())

    def testChatId(self):
        self.assertEqual("ChatId", self.message1._chat_id)

    def testSendTime(self):
        self.assertEqual("26521758127878", self.message1._send_time)

    def testSenderUser(self):
        self.assertEqual("UserId", self.message1._sender_user)

    def testBody(self):
        self.assertEqual("It is my message", self.message1._body)

    def testMessageToXml(self):
        message_xml = self.message1.__toXml__()
        result_message = message.parseMessage(message_xml)
        result_message._receive_time = self.message1._receive_time
        
        self.assertEqual(self.message1, result_message)


if __name__ == '__main__':
    unittest.main()
