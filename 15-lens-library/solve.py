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
    try:
        for line in lines:
            data = line.strip()
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def solve_input_1(data):
    answer = 0
    for operation in data.split(','):
        partial = hash(operation)
        print(f'{operation} -> {partial}')
        answer += partial
    return answer


def hash(data):
    answer = 0
    for char in data:
        answer += ord(char)
        answer *= 17
        answer %= 256
    return answer

def solve_input_2(data):
    answer = 0
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
