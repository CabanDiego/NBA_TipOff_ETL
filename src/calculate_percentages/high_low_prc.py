'''Module to return highest and lowest tip off win percentage'''
from typing import Dict

def highest_percentage(percentages: Dict)-> float:
    '''Return highest tip off win percentage'''
    return max(percentages.values())

def lowest_percentage(percentages: Dict)-> float:
    '''Return lowest tip off win percentage'''
    return min(percentages.values())
