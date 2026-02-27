'''Module to calculate each team's tip off win percentage'''
import logging
from pathlib import Path
from typing import Dict
import pandas as pd

logger = logging.getLogger(__name__)

def calc_win_perc(source: Path)-> Dict:
    '''Return dictionary of each team win percentage'''
    #Checking to see if filtered file was created successfully
    if not source.exists():
        logger.error(f"Source file does not exist: {source}")
        raise FileNotFoundError(f"{source} not found")

    logger.info("Calculating each team's Tip Off Wins")
    df = pd.read_csv(source)

    #Storing amount of tip_offs each team has won
    to_wins = df['player3_team_abbreviation'].value_counts()

    logger.info("Calculating each team's total games played")
    
    #Checking to see if file with teams exists
    teams_file = Path("nba_data/raw/team.csv")
    if not teams_file.exists():
        logger.error(f"Teams file does not exist: {teams_file}")
        raise FileNotFoundError(f"{teams_file} not found")
    
    #Storing teams
    teamsdf = pd.read_csv(teams_file)
    teams = teamsdf['abbreviation'].tolist()

    games_played = {}
    #Looping through teams and finding the number of games played
    for team in teams:
        games_played[team] = df[(df['player1_team_abbreviation'] == team) |
                               (df['player2_team_abbreviation'] == team) ].shape[0]

    logger.info("Calculating and saving percentages to dictionary")
    #Creating new Dict with each team abbreviation as the key, and tip off win % as value
    tip_off_win_perc = {team: float(round(to_wins.get(team, 0) / games_played[team] * 100, 2))
                    for team in teams}

    return tip_off_win_perc
