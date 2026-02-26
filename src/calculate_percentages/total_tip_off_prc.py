'''Module to calculate each team's tip off win percentage'''
import pandas as pd
from pathlib import Path
from typing import Dict

def calc_win_perc(source: Path)-> Dict:
    '''Return dictionary of each team win percentage'''
    df = pd.read_csv(source)
    
    #Storing amount of tip_offs each team has won
    to_wins = (df['player3_team_abbreviation'].value_counts())
    
    #Storing teams
    teamsdf = pd.read_csv("nba_data/raw/team.csv")
    teams = teamsdf['abbreviation'].tolist()
    
    games_played = {}
    #Looping through teams and finding the number of games played
    for team in teams:
        games_played[team] = df[(df['player1_team_abbreviation'] == team) |
                               (df['player2_team_abbreviation'] == team) ].shape[0]
        
    #Creating new Dict with each team abbreviation as the key, and tip off win % as value
    tip_off_win_perc = {team: f"{(to_wins.get(team, 0) / games_played[team] * 100):.2f}%"
                    for team in teams}
    
    return tip_off_win_perc