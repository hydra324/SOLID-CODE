class TimeStamp:
    def __init__(self,timestamp_str) -> None:
        self.timestamp_str = timestamp_str
    
    def get_hour():
        pass

    def get_min():
        pass

    def get_day():
        pass

class Message:
    def __init__(self) -> None:
        self.timestamp = None
        self.text = None
        self.full_message = None

from abc import ABC, abstractmethod

class MessageParser(ABC):

    @abstractmethod
    def parse_message(self,message):
        pass

class DefaultMessageParser(MessageParser):

    def __init__(self,pattern) -> None:
        self.pattern = pattern

    def parse_message(self, message):
        # returns Message
        # makes use of pattern to parse
        pass

class MyDataFrame:
    def __init__(self) -> None:
        self.map = {} # (column:)
    
    def add_message(self,message):
        # add message by text
        pass

    def filter(self,column,value):
        pass
        

from collections import defaultdict
class LogParser:
    def __init__(self,message_parser: MessageParser, df) -> None:
        self.map = defaultdict()
        self.message_parser = message_parser
        self.parsed_df = df

    def contains_pattern(self,message):
        # tells whether message contains pattern
        pass
    def parse_message(self,message):
        pass

    def parse(self,log_file):
        f_open = open(log_file,'r')
        for line in f_open:
            # parse this line
            # self.parse_message(line)
            if not self.contains_pattern(line):
                continue
            message = self.message_parser.parse_message(line)
            df.add(message)
        f_open.close()



        # extarct coutns
        # exctarct hist
        # write to file


