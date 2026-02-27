'''Module to return highest and lowest tip off win percentage'''
from typing import Dict

def highest_percentage(percentages: Dict):
    '''Return highest tip off win percentage'''
    highest_percent = max(percentages.values())
    team =  [t for t, val in percentages.items() if val == highest_percent]
    return print(team , ": ",  highest_percent)

def lowest_percentage(percentages: Dict):
    '''Return lowest tip off win percentage'''
    lowest_percent = min(percentages.values())
    team =  [t for t, val in percentages.items() if val == lowest_percent]
    return print(team , ": ", lowest_percent)
