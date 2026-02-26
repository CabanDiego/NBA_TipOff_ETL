'''Module to run the pipeline'''
from pathlib import Path
from filter_data.filter_tip_off import filter_tip_off
from calculate_percentages.total_tip_off_prc import calc_win_perc
from calculate_percentages.high_low_prc import highest_percentage, lowest_percentage

def run_pipeline(source: Path):
    '''Run Pipeline'''
    filtered_data = filter_tip_off(source)
    win_percentages = calc_win_perc(filtered_data)
    print(win_percentages)
    print("Highest Percentage: ", highest_percentage(win_percentages))
    print("Lowest Percentage: ", lowest_percentage(win_percentages))
