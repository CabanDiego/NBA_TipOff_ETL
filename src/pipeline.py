'''Module to run the pipeline'''
from pathlib import Path
from typing import Dict
from filter_data.filter_tip_off import filter_tip_off
from calculate_percentages.total_tip_off_prc import calc_win_perc

def run_pipeline(source: Path):
    '''Run Pipeline'''
    filtered_data = filter_tip_off(source)
    win_percentages = calc_win_perc(filtered_data)
    print(win_percentages)
    return None