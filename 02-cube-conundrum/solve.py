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
            if which_color == 'red' and int(number) > max_red:
                return False
            if which_color == 'green' and int(number) > max_green:
                return False
            if which_color == 'blue' and int(number) > max_blue:
                return False
    return True


def solve_input_2(data):
    answer = 0
    for game, sets in data.items():
        r, g, b = find_fewest_cubes(sets)
        answer += r * g * b
    return answer

def find_fewest_cubes(sets):
    max_red = max_green = max_blue = 0
    for set in sets:
        colors = set.split(',')
        for color in colors:
            number, which_color = color.split()
            number = int(number)
            if which_color == 'red':
                max_red = max(number, max_red)
            if which_color == 'green':
                max_green = max(number, max_green)
            if which_color == 'blue':
                max_blue = max(number, max_blue)
    return max_red, max_green, max_blue

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
