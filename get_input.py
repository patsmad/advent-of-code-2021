import requests
import json

with open('headers.json', 'r') as f:
    headers = json.load(f)

def get_input(day):
    return requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers=headers)