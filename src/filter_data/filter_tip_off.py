'''Module to filter nba file to a csv with only game start tip offs'''
import pandas as pd
from pathlib import Path

def filter_tip_off(source: Path) -> Path:
    '''Filter play_by_play into Starting Tip Offs only'''
    #Create DF from the play_by_play and teams csv
    df = pd.read_csv(source)
    teamsdf = pd.read_csv("nba_data/raw/team.csv")
    gamesdf = pd.read_csv("nba_data/raw/game.csv")
    
    #Removing all star games
    gamesdf = gamesdf[gamesdf['season_type'] != 'All Star']
    
    #Filtering play_by_play into tip offs and current teams only
    filtered_df = df[
        #Tip_Off event
        (df['eventmsgtype'] == 10) & 
        #First quarter
        (df['period'] == 1) & 
        #Current teams only
        (df['player3_team_abbreviation'].isin(teamsdf['abbreviation']))&
        #Remove All Star games
        df['game_id'].isin(gamesdf['game_id'])]
    
    #Create csv from filtered DF
    output_path = Path("./nba_data/filtered/filtered_tip_off.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    filtered_df.to_csv(output_path, index=False)
    
    return output_path
