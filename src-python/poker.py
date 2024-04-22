"""Poker Hand



You want to create a method that receives a hand of 5 cards and returns the best poker hand you can make with those cards.
For simplification, we'll assume cards have a number and a symbol. Numbers go from 1 to 10 and symbols are 'a', 'b', 'c' and 'd'.
To start off, assume there are only 3 types of poker hands, from better to worse. Take into consideration you will have to add the other ones later.
- Flush: 5 cards of the same symbol. Example: 10a 4a 2a 7a 9a
- Three of a Kind: 3 cards with the same number. Example: 4a 3b 1c 4d 4b
- Pair: Two cards with the same number. Example: 3a 2b 8d 1a 8c
Return the best poker hand you have. For example. If you have a pair, return "Pair" or any structure that symbolizes you have a pair. If you have a three of a kind, return "Three of a Kind" or any structure that represents it.
Notes:
- This question is best suited for Logical and Maintainable as it has a very low Problem Solving but a good solution requires good modularized code
- Don't ask the candidate to code the entire evaluation of all hands. Only a few are good enough. The important part of this problem is code organization
Follow Up Questions




- Let's say we introduce a new type of hand. How would you add it?
- Full House: Having both a pair and a three of a kind. Example: 2a 3a 3b 2c 2d
- Let's say we introduce the additional rule that every round there's a "lucky hand" that wins over all the other ones for that round only. So if a Two Pair gets picked as the lucky hand, it wins against all other hands, but next round a Flush might be the lucky hand. How would you add this change?
Common Expected Good Solutions



This is a rule evaluation problem. A good candidate would separate rule evaluation from each individual rule implementation. Optimally using interfaces or any similar mechanism to generalize rules.
A good solution would be to:
1. Create a rule interface
2. Code each hand evaluation an implementation of this interface
3. Create a list of these rules in order of priority and evaluate the hand input against each rule, returning when one matches
4. Having a default rule when none matches
Also a good candidate would encapsulate the cards and hand in some structure that holds the cards.
For example:
public class Card {
    private int value;
    private String symbol;
}
"""
from typing import List
from collections import defaultdict
import random

class Card:
    def __init__(self,value: int, symbol: str) -> None:
        self.value = value
        self.symbol = symbol
    
    def __repr__(self) -> str:
        return f"[{self.value,self.symbol}]"

class Hand:
    """ represnets the deck of cards a player has in their hands """
    
    def __init__(self,hand: List[Card] = []) -> None:
        self.hand = hand

    def get_size(self):
        return len(self.hand)
    
    def get(self,index):
        return self.hand[index]

    def add(self,card: Card):
        """ method for performing crud operarations on hand """
        self.hand.append(card)

    def __iter__(self):
        self.iter = 0
        return self
    
    def __next__(self):
        self.iter += 1
        if self.iter<len(self.hand):
            return self.hand[self.iter]
        else:
            raise StopIteration

    def __repr__(self):
        out_str = ""
        for card in self.hand:
            out_str += str(card) + ","
        return out_str[:-1]

from abc import ABC, abstractmethod
class IRule(ABC):
    """ Rule interface """
    @abstractmethod
    def evaluate(self, hand: Hand) -> bool:
        pass

    def get_rule_name(self) -> str:
        pass
    
class FlushRule(IRule):
    def evaluate(self, hand: Hand) -> bool:
        symbolToCompare = hand.get(0).symbol
        symbolCount = 0
        for card in hand:
            symbolCount += int(symbolToCompare==card.symbol)
        return symbolCount >= 5
    
    def get_rule_name(self):
        return "FLUSH"
    
class ThreeOfAKindRule(IRule):
    def evaluate(self, hand: Hand) -> bool:
        frequency_map = defaultdict(int)
        for card in hand:
            frequency_map[card.value] += 1
            if frequency_map[card.value]==3:
                return True
        return False
    
    def get_rule_name(self) -> str:
        return "THREE_OF_A_KIND"

class PairRule(IRule):
    def evaluate(self, hand: List[Card]) -> bool:
        frequency_map = defaultdict(int)
        for card in hand:
            frequency_map[card.value] += 1
            if frequency_map[card.value]==2:
                return True
        return False
    
    def get_rule_name(self) -> str:
        return "PAIR"

class Game:
    def __init__(self,hand: Hand,rules: List[IRule]) -> None:
        
        self.hand = hand
        self.rules = rules

    

    def rearrange_rules(self,luckyrule):
        self.rules.pop(self.rules.index(luckyrule))
        self.rules = [luckyrule] + self.rules

    def check_if_winning(self,luckyrule: IRule = None) -> str:
        if luckyrule:
            self.rearrange_rules(luckyrule)
        winning_rule = None
        for rule in self.rules:
            if rule.evaluate(self.hand):
                winning_rule = rule
                break
        if not winning_rule:
            return "No rule matches for the current hand"
        return f"{rule.get_rule_name()} rule matches with the hand: {self.hand}"
    
def build_random_cards():
    set_of_symbols = ['A','B','C','D']
    hand = Hand()
    while hand.get_size()<5:
        random_value = int(11*random.random())+1
        random_symbol = set_of_symbols[int((4)*random.random())]
        hand.add(Card(random_value,random_symbol))
    return hand

if __name__ == '__main__':
    rules = [FlushRule(),ThreeOfAKindRule(),PairRule()]
    for _ in range(10):
        game = Game(build_random_cards(),rules)
        print(game.check_if_winning())
    

            