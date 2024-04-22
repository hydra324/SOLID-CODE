"""
Example Question #1

At Amazon.com, we send emails and SMS messages customers every day.
Example messages like order confirmation and daily lightning deals offers etc..

Design an API that:
    Takes requests from internal systems like orders, marketing, payments, etc.
    Sends messages (email, SMS, or both) out to customers based on the request.

Extension:

Support Whatsapp, Facebook Messenger messages.
Millions TPS.
Handle messages with different priorities.

Meets Bar:
Meets almost all of the following.

Asks clarification questions like: traffic, latency, dependencies
Writes extendable classes/interfaces and reusable methods/functions
Create simple and maintainable code for the requirements, no over-engineering
Code is syntactically correct or would be syntactically correct with minor improvements
No or minor syntax 

RAISES Bar:

Meets any of the following.

Meets all in "Meets Bar".
Came up solution quick with context and able to expand on that quickly

Lowers Bar:
Meets two or more of the following.

Creates unnecessarily complex code (e.g., doesn't consider reuse, poorly formatted, contains improper coding constructs)
Creates Difficult to maintain code (e.g., difficult to trace impact of changes, poor variable naming conventions)
Code is organized in a way that is difficult to read and understands
Code contains major syntax errors or is in pseudo-code
Code doesn't work as intended

"""

from abc import ABC,abstractmethod
from enum import Enum
import json

class Channel(Enum):
    DEFAULT = 0
    EMAIL = 1
    SMS = 2

class IMessage(ABC):
    def __init__(self,id,message) -> None:
        super().__init__()
        self.id = id
        self.message = message

    @abstractmethod
    def __repr__(self) -> str:
        return f"message id: {self.id} and message: {self.message}"

class EmailMessage(IMessage):
    def __init__(self, id, message, email) -> None:
        super().__init__(id, message)
        self.email = email

    def __repr__(self) -> str:
        return f"Email message {super().__repr__()} to {self.email}"

class SMSMessage(IMessage):
    def __init__(self, id, message, mobileNumber) -> None:
        super().__init__(id, message)
        self.mobileNumber = mobileNumber

    def __repr__(self) -> str:
        return f"SMS message {super().__repr__()} to {self.mobileNumber}"

class BaseNotificationHandler(ABC):

    @abstractmethod
    def send(self,message: IMessage):
        print(f"sent {message}")

    @abstractmethod
    def getChannel(self):
        return Channel.DEFAULT

class EmailNotificationHandler(BaseNotificationHandler):
    def send(self,message: EmailMessage):
        # do custom logic for sending email (maybe through 3rd party)
        print(f"sent {message}")

    def getChannel(self):
        return Channel.EMAIL

class SMSNotificationHandler(BaseNotificationHandler):
    def send(self, message: SMSMessage):
        # do custom logic sending for SMS email sending
        print(f"sent {message}")

    def getChannel(self):
        return Channel.SMS

# singleton
class NotificationHandlerFactory:
    def __init__(self) -> None:
        self.handlers = {}

    def add(self, handler: BaseNotificationHandler):
        self.handlers[handler.getChannel()] = handler

    def getHandler(self, channel: Channel):
        return self.handlers.get(channel)

class MessageService:
    def __init__(self, notificationHandlerFactory) -> None:
        self.notificationHandlerFactory =  notificationHandlerFactory


    def sendNotifications(self,messagesToSend: str):
        messagesToSend = json.loads(messagesToSend)
        # some how construct messages from above and send notification
        for message in messagesToSend:
            if message['channel']=='email':
                msg = EmailMessage(id=message['id'],message=message['message'],email=message['email'])
                handler = self.notificationHandlerFactory.getHandler(Channel.EMAIL)
                handler.send(msg)
            if message['channel']=='sms':
                msg = SMSMessage(id=message['id'],message=message['message'],mobileNumber=message['mobileNumber'])
                handler = self.notificationHandlerFactory.getHandler(Channel.SMS)
                handler.send(msg)
            

# driver code        
handlerFactory=NotificationHandlerFactory()
handlerFactory.add(SMSNotificationHandler())
handlerFactory.add(EmailNotificationHandler())
messageService = MessageService(handlerFactory)

# client requirements
messagesToSend = [
    {
        'id': "1",
        'channel':'email',
        'message':'hello how is it going?',
        'email':'test@test.com'
    },
    {
        'id':"2",
        'channel':'sms',
        'message':'whats gwan bruh?',
        'mobileNumber':'9793448789'
    }
]

# client calls send
messageService.sendNotifications(json.dumps(messagesToSend))