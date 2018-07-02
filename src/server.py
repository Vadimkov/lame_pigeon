from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

from user import UserManager
from user import User

from chat import Chat
from chat import ChatManager


class MessageProtocol(Protocol):

    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.state = "LOGGING_IN"
        print("Started")

    def connectinMade(self):
        print("connection made")

    def connectionLost(self, reason):
        if self.name in self.factory.users:
            del(self.factory.users[self.name])

    def dataReceived(self, data):
        print("Data received")
        

    def handle_LOGIN(self, mes):
        print("Logging in")


class ClientFactory(Factory):
    
    def __init__(self):
        self.clients = {}
        self.um = UserManager()
        self.cm = ChatManager(self)

    def buildProtocol(self, addr):
        return MessageProtocol(self)

print("Try start")
reactor.listenTCP(8000, ClientFactory())
reactor.run()