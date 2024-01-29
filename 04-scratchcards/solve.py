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

def parse_input(lines):
    data = {}
    try:
        for line in lines:
            card, rest = line.strip().split(':')
            winning, have = rest.split("|")
            data[card] = [sorted(int(x) for x in winning.split()), sorted(int(x) for x in have.split())]
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def solve_input_1(cards):
    answer = 0
    for card, numbers in cards.items():
        partial = 0
        winning, have = numbers
        for number in winning:
            i = bisect.bisect_left(have, number)
            if i >= len(have):
                continue
            if number == have[i]:
                '''print('---')
                print(winning)
                print(have)
                print(number)
                print(i)'''
                if not partial:
                    partial = 1
                else:
                    partial *= 2
        answer += partial
    return answer

def solve_input_2(data):
    answer = data
    return answer

try:
    assert 'input' in sys.argv[-2]
    assert sys.argv[-1] in ['1', '2']
    if '1' == sys.argv[-1]:
        data = parse_input(fileinput.input())
        answer = (solve_input_1(data))
        print(answer)
    elif '2' == sys.argv[-1]:
        data = parse_input(fileinput.input())
        answer = (solve_input_2(data))
        print(answer)
    else:
        print(usage)
except (RuntimeError, AssertionError, IndexError) as e:
    print(usage, e)
