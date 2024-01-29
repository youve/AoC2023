#!/usr/bin/env python3

import bisect
import fileinput
import sys
import functools
import math
import dataclasses
from hashlib import sha256

usage = '''
Usage:
    solve.py input 1
    solve.py input 2
'''

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.rank = self.rank_self()
        self.card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def rank_self(self):
        if self.is_five_of_a_kind():
            return 7
        elif self.is_four_of_a_kind():
            return 6
        elif self.is_full_house():
            return 5
        elif self.three_of_a_kind():
            return 4
        elif self.two_pair():
            return 3
        elif self.one_pair():
            return 2
        elif self.high_card():
            return 1
        else:
            return 0

    def is_five_of_a_kind(self):
        return len(set(self.cards)) == 1

    def is_four_of_a_kind(self):
        uniq = set(self.cards)
        for card in uniq:
            if self.cards.count(card) == 4:
                return True
        return False

    def is_full_house(self):
        uniq = set(self.cards)
        if len(uniq) != 2:
            return False
        two = three = False
        for card in uniq:
            if self.cards.count(card) == 2:
                two = True
            elif self.cards.count(card) == 3:
                three = True
            else:
                return False
        return two and three

    def three_of_a_kind(self):
        uniq = set(self.cards)
        for card in uniq:
            if self.cards.count(card) == 3:
                return True
        return False

    def two_pair(self):
        pairs = 0
        uniq = set(self.cards)
        for card in uniq:
            if self.cards.count(card) == 2:
                pairs += 1
        return pairs == 2

    def one_pair(self):
        uniq = set(self.cards)
        for card in uniq:
            if self.cards.count(card) == 2:
                return True
        return False

    def high_card(self):
        return len(set(self.cards)) == 5

    def compare_cards(self, a, b):
        return self.card_values.index(a) > self.card_values.index(b)

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        if self.rank == other.rank:
            for i in range(5):
                if self.cards[i] == other.cards[i]:
                    continue
                return self.compare_cards(self.cards[i], other.cards[i])
        return False

class JokerHand(Hand):
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.rank = self.rank_self()
        self.card_values = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    def is_five_of_a_kind(self):
        cards = set(self.cards)
        if 'J' in cards:
            cards.remove('J')
        return len(set(self.cards)) == 1

    def is_four_of_a_kind(self):
        uniq = set(self.cards)
        for card in uniq:
            if card != 'J':
                if self.cards.count(card) + self.cards.count('J') >= 4:
                    return True
            else:
                return self.cards.count('J') == 4
        return False

    def is_full_house(self):
        uniq = set(self.cards)
        if len(uniq) != 2 or ('J' in uniq and len(uniq) != 3):
            return False
        two = three = False
        for card in uniq:
            if self.cards.count(card) == 2:
                two = True
            elif self.cards.count(card) == 3:
                three = True
            else:
                if 'J' not in uniq:
                    return False
        if self.__super__(self.three_of_a_kind()) or self.__super__(self.two_pair()) and 'J' in self.cards:
            return True
        return two and three

    def three_of_a_kind(self):
        uniq = set(self.cards)
        for card in uniq:
            if card != 'J':
                if self.cards.count(card) + self.cards.count('J') >= 3:
                    return True
            else:
                return self.cards.count('J') == 3
        return False

    def two_pair(self):
        pairs = 0
        uniq = set(self.cards)
        for card in uniq:
            if self.cards.count(card) == 2:
                pairs += 1
        if pairs == 2:
            return True
        if 'J' in self.cards and pairs == 1:
            return True
        if self.cards.count('J') == 2:
            return True
        return False

    def one_pair(self):
        uniq = set(self.cards)
        for card in uniq:
            if self.cards.count(card) == 2:
                return True
        if 'J' in uniq:
            return True
        return False

    def high_card(self):
        return len(set(self.cards)) == 5


def parse_input_1(lines):
    data = []
    try:
        for line in lines:
            line = line.strip()
            cards, bid = line.split()
            hand = Hand(cards, bid)
            bisect.insort(data, hand)
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def parse_input_2(lines):
    data = []
    try:
        for line in lines:
            line = line.strip()
            cards, bid = line.split()
            hand = JokerHand(cards, bid)
            bisect.insort(data, hand)
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def solve_input_1(hands):
    answer = 0
    for i, hand in enumerate(hands):
        rank = i + 1
        answer += (rank * hand.bid)
    return answer

def solve_input_2(data):
    #4794 is too low
    return solve_input_1(data)

try:
    assert 'input' in sys.argv[-2]
    assert sys.argv[-1] in ['1', '2']
    if '1' == sys.argv[-1]:
        data = parse_input_1(fileinput.input())
        answer = (solve_input_1(data))
        print(answer)
    elif '2' == sys.argv[-1]:
        data = parse_input_2(fileinput.input())
        answer = (solve_input_2(data))
        print(answer)
    else:
        print(usage)
except (RuntimeError, AssertionError, IndexError) as e:
    print(usage, e)
    raise
