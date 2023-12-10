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
            data.append([int(x) for x in line.strip().split()])
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def solve_input_1(data):
    answer = 0
    for line in data:
        answer += solve_arithmetic_sequence_1(line)
    return answer

def solve_arithmetic_sequence_1(line):
    if len(set(line)) == 1:
        return line[-1]
    else:
        new_line = []
        for i in range(1, len(line)):
            new_line.append(line[i] - line[i - 1])
        return line[-1] + solve_arithmetic_sequence_1(new_line)

def solve_input_2(data):
    answer = 0
    for line in data:
        answer += solve_arithmetic_sequence_2(line)
    return answer

def solve_arithmetic_sequence_2(line):
    if len(set(line)) == 1:
        return line[0] - (line[1] - line[0])
    else:
        new_line = []
        for i in range(1, len(line)):
            new_line.append(line[i] - line[i - 1])
        return line[0] - solve_arithmetic_sequence_2(new_line)

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
