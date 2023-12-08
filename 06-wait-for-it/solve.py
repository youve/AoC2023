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

def parse_input_1(lines):
    times = []
    distances = []
    data = {}
    try:
        for line in lines:
            line = line.strip()
            if line.startswith('Time'):
                times = [int(x) for x in line.split(':')[1].split()]
                print(times)
            else:
                distances = [int(x) for x in line.split(':')[1].split()]
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    data = dict(zip(times, distances))
    return data

def parse_input_2(lines):
    try:
        for line in lines:
            if line.startswith('Time'):
                time = int(''.join(line.split(':')[1].split()))
            else:
                distance = int(''.join(line.split(':')[1].split()))
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return {time : distance}

def solve_input_1(data):
    answer = 0
    print(data)
    for race in data.items():
        time, distance = race
        l = get_lowest(time, distance)
        if not l:
            continue
        u = get_highest(time, distance)
        partial = u - l + 1
        if not answer:
            answer = 1
        answer *= partial
    return answer

def get_lowest(time, distance):
    for start in range(2, time - 2):
        if (time - start) * start > distance:
            return start

def get_highest(time, distance):
    for start in range(time - 2, 2, -1):
        if (time - start) * start > distance:
            return start

def solve_input_2(data):
    return solve_input_1(data)

try:
    assert 'input' in sys.argv[-2]
    assert sys.argv[-1] in ['1', '2']
    if '1' == sys.argv[-1]:
        data = parse_input_1(fileinput.input())
        print(data)
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
