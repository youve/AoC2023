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
            game, sets = line.strip().split(':')
            game = int(game.split()[1])
            data[game] = sets.split(';')
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def solve_input_1(data):
    answer = 0
    for game, sets in data.items():
        if is_valid(sets):
            answer += game
    return answer

def is_valid(sets):
    max_red = 12
    max_green = 13
    max_blue = 14
    for set in sets:
        colors = set.split(',')
        for color in colors:
            number, which_color = color.split()
            if which_color == 'red' and int(number) > 12:
                return False
            if which_color == 'green' and int(number) > 13:
                return False
            if which_color == 'blue' and int(number) > 14:
                return False
    return True


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
