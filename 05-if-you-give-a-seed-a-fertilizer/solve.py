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
    data = {
        'seeds': [],
        'seed_to_soil': {},
        'soil_to_fertilizer': {},
        'fertilizer_to_water': {},
        'water_to_light': {},
        'light_to_temperature': {},
        'temperature_to_humidity': {},
        'humidity_to_location' : {}
    }
    current_task = 'seeds'
    try:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if current_task == 'seeds':
                if line.startswith('seed-to-soil'):
                    current_task = 'seed_to_soil'
                else:
                    data['seeds'] = [int(x) for x in line.split(': ')[1].split()]
            elif current_task == 'seed_to_soil':
                if line.startswith('soil'):
                    current_task = "soil_to_fertilizer"
                else:
                    populate_dictionary(data, 'seed_to_soil', line)
            elif current_task == 'soil_to_fertilizer':
                if line.startswith('fert'):
                    current_task = 'fertilizer_to_water'
                else:
                    populate_dictionary(data, 'soil_to_fertilizer', line)
            elif current_task == "fertilizer_to_water":
                if line.startswith('water'):
                    current_task = 'water_to_light'
                else:
                    populate_dictionary(data, 'fertilizer_to_water', line)
            elif current_task == "water_to_light":
                if line.startswith('light'):
                    current_task = 'light_to_temperature'
                else:
                    populate_dictionary(data, 'water_to_light', line)
            elif current_task == "light_to_temperature":
                if line.startswith('temperature'):
                    current_task = 'temperature_to_humidity'
                else:
                    populate_dictionary(data, 'light_to_temperature', line)
            elif current_task == "temperature_to_humidity":
                if line.startswith('humidity'):
                    current_task = 'humidity_to_location'
                else:
                    populate_dictionary(data, 'temperature_to_humidity', line)
            elif current_task == "humidity_to_location":
                populate_dictionary(data, 'humidity_to_location', line)
    except FileNotFoundError:
        # Using fileinput is so handy but I also want to specify part 1 or part 2 from the command line
        pass
    return data


def populate_dictionary(d, key, line):
    dst, src, length = line.split()
    src = int(src)
    dst = int(dst)
    length = int(length)
    while length > 0:
        d[key][src] = dst
        src += 1
        dst += 1
        length -= 1

def seed_to_location(data, seed):
    '''
        'seed_to_soil': {},
        'soil_to_fertilizer': {},
        'fertilizer_to_water': {},
        'water_to_light': {},
        'light_to_temperature': {},
        'temperature_to_humidity': {},
        'humidity_to_location' : {}
    '''
    soil = data['seed_to_soil'].get(seed, seed)
    fertilizer = data['soil_to_fertilizer'].get(soil, soil)
    water = data['fertilizer_to_water'].get(fertilizer, fertilizer)
    light = data['water_to_light'].get(water, water)
    temperature = data['light_to_temperature'].get(light, light)
    humidity = data['temperature_to_humidity'].get(temperature, temperature)
    location = data['humidity_to_location'].get(humidity, humidity)
    #print(f'seed: {seed} -> soil {soil} -> fertilizer{fertilizer} -> light {light} -> temperature {temperature} -> humidity {humidity} -> location {location}')
    return location

def solve_input_1(data):
    answer = -1
    for seed in data['seeds']:
        result = seed_to_location(data, seed)
        if answer < 0:
            answer = result
        else:
            answer = min(result, answer)
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
    raise
