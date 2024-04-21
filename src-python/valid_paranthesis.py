# today we're designing a valid paranthesis checker class
# the requirements are as follows:
# 1. the class takes in a string
# 2. method which spits out whether it is a valid paranthesis or not
# focus should be on logical and manitanable code
# consider extensibility of your code

from abc import ABC, abstractmethod
class BracketService(ABC):

    @abstractmethod
    def get_open_bracket(self,ch):
        pass

    @abstractmethod
    def is_valid_open(self,ch):
        pass

    @abstractmethod
    def is_valid_close(self,ch):
        pass

class RegularBracket(BracketService):
    def __init__(self) -> None:
        self.mapping = {}
        self.open_bracket = set()

    def add_bracket_pair(self,open,close):
        self.open_bracket.add(open)
        self.mapping[close] = open

    def is_valid_close(self,ch):
        return ch in self.mapping
        
    def get_open_bracket(self,ch):
        return self.mapping.get(ch)
    
    def is_valid_open(self,ch):
        return ch in self.open_bracket


# ()

# ) -> (

class ValidParanthesis:
    def __init__(self,bracket_service: BracketService):
        self._stack = [] # private member
        self.bracket_service = bracket_service

    def is_valid(self,input_str: str) -> bool:
        for ch in input_str:
            if self.bracket_service.is_valid_open(ch):
                self._stack.append(ch)
                continue
            
            if (not self._stack) or \
                (not self.bracket_service.is_valid_close(ch)) or \
                (self.bracket_service.get_open_bracket(ch)!=self._stack[-1]):
                return False
            self._stack.pop()
        return not self._stack
    def clear(self):
        self._stack = []
    
if __name__ == '__main__':
    bracket_service  = RegularBracket()
    bracket_service.add_bracket_pair("(",")")
    bracket_service.add_bracket_pair("{","}")
    bracket_service.add_bracket_pair("[","]")
    bracket_service.add_bracket_pair("A","B")
    valid_paranthesis = ValidParanthesis(bracket_service)

    def test_string(s: str):
        print(f"answer for string {s} is",valid_paranthesis.is_valid(s))
    
    test_cases = [
        "((])",
        "",
        "(())",
        "{[()]}",
        "{A)}",
        "ABABBA",
        "(AB)"
    ]

    for test in test_cases:
        valid_paranthesis.clear()
        test_string(test)

