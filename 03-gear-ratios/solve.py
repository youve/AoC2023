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
            data.append([c for c in line.strip()])
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data

def get_all_neighbours(col, row, data):
    max_y = len(data) - 1
    max_x = len(data[0]) - 1
    n = []
    for x in range(col - 1, col + 2):
        if x < 0 or x > max_x:
            continue
        for y in range(row - 1, row + 2):
            if y < 0 or y > max_y:
                continue
            n.append((x,y))
    return n

def seek_left(x, y, data):
    '''
    Return the start of a number
    '''
    while x >= 0 and data[y][x].isnumeric():
        x -= 1
    x += 1
    return (x, y)

def seek_right(x, y, data):
    '''
    Return the end of a number
    '''
    while x < len(data[y]) and data[y][x].isnumeric():
        x += 1
    x -= 1
    return (x, y)

def get_number(start, end, data):
    start_x, start_y = start
    end_x, end_y = end
    return int(''.join(data[end_y][start_x:end_x+1]))

def solve_input_1(data):
    answer = 0
    number_starts = set()
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell.isnumeric() or cell == '.':
                continue
            candidates = get_all_neighbours(x, y, data)
            print(f'exploring cell {cell} at {x, y}, found candidates {candidates}')
            for candidate in candidates:
                c_x, c_y = candidate
                if data[c_y][c_x].isnumeric():
                    l = seek_left(c_x, c_y, data)
                    r = seek_right(c_x, c_y, data)
                    print(f'found a number at {c_y, c_x}, it starts at {l}')
                    print(f'it ends at {r} and its value is {get_number(l, r, data)}')
                    number_starts.add(seek_left(c_x, c_y, data))
    for start in number_starts:
        x, y = start
        end = seek_right(x, y, data)
        number = get_number(start, end, data)
        print(number)
        # 633 is missed, 58 is mistakenly counted
        answer += number
    return answer

def solve_input_2(data):
    # 52835462 is too low
    answer = 0
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell.isnumeric() or cell == '.':
                continue
            number_starts = set()
            candidates = get_all_neighbours(x, y, data)
            print(f'exploring cell {cell} at {x, y}, found candidates {candidates}')
            for candidate in candidates:
                c_x, c_y = candidate
                if data[c_y][c_x].isnumeric():
                    l = seek_left(c_x, c_y, data)
                    r = seek_right(c_x, c_y, data)
                    print(f'found a number at {c_y, c_x}, it starts at {l}')
                    print(f'it ends at {r} and its value is {get_number(l, r, data)}')
                    number_starts.add(seek_left(c_x, c_y, data))
            if len(number_starts) == 2:
                partial_answer = 1
                for start in number_starts:
                    x, y = start
                    end = seek_right(x, y, data)
                    number = get_number(start, end, data)
                    partial_answer *= number
        # 633 is missed, 58 is mistakenly counted
                answer += partial_answer
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
