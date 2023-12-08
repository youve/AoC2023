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
    data = []
    try:
        for line in lines:
            data.append(line.strip())
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def solve_input_1(data):
    answer = 0
    for line in data:
        start = ''
        end = ''
        for char in line:
            if char.isnumeric():
                start = char
                break
        for char in reversed(line):
            if char.isnumeric():
                end = char
                break
        answer += int(start + end)
    return answer

def solve_input_2(data):
    answer = 0
    start_strings = {'one' : '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    end_strings = {x[::-1] : y for x,y in start_strings.items()}
    for line in data:
        start_index = len(line)
        end_index = len(line)
        start_value = ''
        end_value = ''
        for s in list(start_strings.keys()) + list(start_strings.values()):
            if s in line:
                i = line.index(s)
                start_index = min(start_index, i)
                if start_index == i:
                    if s.isnumeric():
                        start_value = s
                    else:
                        start_value = start_strings[s]
        line = line[::-1]
        for e in list(end_strings.keys()) + list(end_strings.values()):
            if e in line:
                i = line.index(e)
                end_index = min(end_index, i)
                if end_index == i:
                    if e.isnumeric():
                        end_value = e
                    else:
                        end_value = end_strings[e]
        answer += int(start_value + end_value)
    return answer


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
