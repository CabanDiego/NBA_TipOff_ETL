'''Module to filter nba file to a csv with only game start tip offs'''
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def filter_tip_off(source: Path) -> Path:
    '''Filter play_by_play into Starting Tip Offs only'''
    #Checking to see if filtered file was created successfully
    if not source.exists():
        logger.error(f"Source file does not exist: {source}")
        raise FileNotFoundError(f"{source} not found")
    
    #Checking to see if file with teams exists
    teams_file = Path("nba_data/raw/team.csv")
    if not teams_file.exists():
        logger.error(f"Teams file does not exist: {teams_file}")
        raise FileNotFoundError(f"{teams_file} not found")
    
    #Checking to see if file with teams exists
    games_file = Path("nba_data/raw/game.csv")
    if not games_file.exists():
        logger.error(f"Teams file does not exist: {games_file}")
        raise FileNotFoundError(f"{games_file} not found")
    
    
    logger.info("Filtering Play_by_Play File")
    #Create DF from the play_by_play and teams csv
    df = pd.read_csv(source)
    teamsdf = pd.read_csv(teams_file)
    gamesdf = pd.read_csv(games_file)
    
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
    
    try:
        filtered_df.to_csv(output_path, index=False)
        logger.info(f"Filtered tip-offs saved to {output_path}")
    except Exception:
        logger.exception(f"Failed to save filtered_df to {output_path}")
        raise
    
    return output_path
