'''Module to run the pipeline'''
from pathlib import Path
from typing import Dict
from filter_data.filter_tip_off import filter_tip_off

def run_pipeline(source: Path):
    '''Run Pipeline'''
    filter_tip_off(source)
    return None