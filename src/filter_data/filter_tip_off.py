'''Module to filter nba file to a csv with only game start tip offs'''
import pandas as pd
from pathlib import Path

def filter_tip_off(source: Path):
    '''Filter play_by_play into Starting Tip Offs only'''
    df = pd.read_csv(source)
    
    filtered_df = df[(df['eventmsgtype'] == 10) & (df['period'] == 1)]
    
    filtered_df.to_csv("./nba_data/filtered/filtered_tip_off.csv", index=False)
    return None

filter_tip_off(source=Path("nba_data/raw/play_by_play.csv"))