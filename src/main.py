'''Main'''
import logging
from pathlib import Path
from logger.logging_config import set_up_logs
from pipeline import run_pipeline

BASEPATH = Path(__file__).resolve().parent.parent
RAWDATA = BASEPATH / "nba_data" / "raw" / "play_by_play.csv"
OUTDIR = BASEPATH / "nba_data"/ "out"
OUTDIR.mkdir(exist_ok=True)

def main():
    '''Main'''
    logger = logging.getLogger(__name__)
    logger.info("Starting ETL pipeline")
    logger.info(f"Input file: {RAWDATA}")
    run_pipeline(RAWDATA)
    logger.info("Pipeline finished successfully")

if __name__ == "__main__":
    set_up_logs()
    main()
