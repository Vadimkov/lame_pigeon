import xml.etree.ElementTree as ET
import time
from enum import Enum
from xml.dom import minidom
from abc import ABC
from abc import abstractmethod


current_milli_time = lambda: int(round(time.time() * 1000))


class MessageType(Enum):
    CHAT = "CHAT"
    SERVICE = "SERVICE"


class ActionType(Enum):
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"
    REGISTER = "REGISTER"
    CREATE_CHAT = "CREATE_CHAT"


def parseMessage(xml_string):
    message = None

    root = ET.fromstring(xml_string)

    if root.attrib['type'] == MessageType.CHAT.value:
        message = xmlToChatMessage(root)
    elif root.attrib['type'] == MessageType.SERVICE.value:
        message = xmlToServiceMessage(root)

    return message

def xmlToChatMessage(root):
    mes = ChatMessage()
    mes._message_type = MessageType.CHAT

    for node in root:
        if node.tag == "destination":
            mes._chat_id = node.attrib['chat_id']
        elif node.tag == "send_time":
            mes._send_time = node.text
        elif node.tag == "sender_user":
            mes._sender_user = node.text
        elif node.tag == "body":
            mes._body = node.text
    
    mes._receive_time = current_milli_time()

    return mes

def xmlToServiceMessage(element):
    mes = None

    # parse action
    action = element.attrib['action']
    if action.attrib['type'] == ActionType.LOGIN.value:
        mes = parseLoginAction(action)
    else:
        raise Exception()

    # parser metainfo
    for node in element:
        if node.tag == "send_time":
            mes._send_time = node.text
        elif node.tag == "sender_user":
            mes._sender_user = node.text

    mes._receive_time = current_milli_time()

    return mes


def parseLoginAction(action):
    mes = LoginMessage()
    return mes


class Message(ABC):
    """<?xml version="1.0" ?>
    <message type="CHAT">
        <destination chat_id="ChatId"/>
        <send_time>26521758127878</send_time>
        <receive_time>527625371587</receive_time>
        <sender_user>UserId</sender_user>
        <body>It is my message</body>
    </message>
    """

    def __init__(self):
        self._message_type = None
        
    def getType(self):
        return self._message_type

    def __repr__(self):
        return minidom.parseString(self.__toXml__()).toprettyxml()

    def __toByte__(self):
        return bytes(self.__toXml__(), 'utf-8')

    @abstractmethod
    def __toXml__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass


class ChatMessage(Message):
    """<?xml version="1.0" ?>
    <message type="CHAT">
        <destination chat_id="ChatId"/>
        <send_time>26521758127878</send_time>
        <receive_time>527625371587</receive_time>
        <sender_user>UserId</sender_user>
        <body>It is my message</body>
    </message>
    """

    def __init__(self):
        Message.__init__(self)
        self._message_type = MessageType.CHAT


    def getBody(self):
        return self._body

    def __toXml__(self):
        root = ET.Element("message")
        root.attrib['type'] = self._message_type.value

        destination = ET.SubElement(root, "destination")
        destination.attrib['chat_id'] = self._chat_id

        send_time = ET.SubElement(root, "send_time")
        send_time.text = str(self._send_time)

        receive_time = ET.SubElement(root, "receive_time")
        receive_time.text = str(self._receive_time)

        sender_user = ET.SubElement(root, "sender_user")
        sender_user.text = self._sender_user

        body = ET.SubElement(root, "body")
        body.text = self._body

        return ET.tostring(root, method='xml', encoding='utf-8')

    def __eq__(self, other):
        if      self.getType() == other.getType()           and \
                self._chat_id == other._chat_id             and \
                self._send_time == other._send_time         and \
                self._receive_time == other._receive_time   and \
                self._sender_user == other._sender_user     and \
                self._body == other._body:
            return True
        return False
        

class ServiceMessage(Message):
    """<?xml version="1.0" ?>
    <message type="SERVICE">
        <send_time>26521758127878</send_time>
        <receive_time>527625371587</receive_time>
        <sender_user>UserId</sender_user>
        <action type="LOGIN"/>
    </message>"""

    def __init__(self):
        Message.__init__(self)
        self._message_type = MessageType.SERVICE

    def _headerToXml(self):
        root = ET.Element("message")
        root.attrib['type'] = self._message_type.value

        send_time = ET.SubElement(root, "send_time")
        send_time.text = str(self._send_time)

        receive_time = ET.SubElement(root, "receive_time")
        receive_time.text = str(self._receive_time)

        sender_user = ET.SubElement(root, "sender_user")
        sender_user.text = self._sender_user

        return root

    def __eq__(self, other):
        return self == other


class LoginMessage(ServiceMessage):
    """<?xml version="1.0" ?>
    <message type="SERVICE">
        <send_time>26521758127878</send_time>
        <receive_time>527625371587</receive_time>
        <sender_user>UserId</sender_user>
        <action type="LOGIN"/>
    </message>"""

    def __init__(self):
        self._action_type = ActionType.LOGIN
        ServiceMessage.__init__(self)

    def __toXml__(self):
        root = self._headerToXml()

        action = ET.SubElement(root, "action")
        action.attrib['type'] = self._action_type.value

        return ET.tostring(root, method='xml', encoding='utf-8')
