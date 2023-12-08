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

@dataclasses.dataclass
class Node:
    name: str
    L: str
    R: str

def parse_input(lines):
    data = {}
    first = True
    try:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if first:
                instructions = line
                data['instructions'] = instructions
                first = False
            else:
                print(line)
                node, children = line.split(' = ')
                left, right = children.replace('(', '').replace(')', '').replace(' ', '').split(',')
                n = Node(node, left, right)
                data[node] = n
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def solve_input_1(data):
    steps = 0
    current = 'AAA'
    while True:
        for instruction in data['instructions']:
            if current == 'ZZZ':
                return steps
            if steps % 1000 == 0:
                print(f'Progress: {steps}')
            steps += 1
            if instruction == 'L':
                current = data[current].L
            else:
                current = data[current].R


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
    raise
