'''Main'''
from pathlib import Path
from pipeline import run_pipeline

BASEPATH = Path(__file__).resolve().parent.parent
RAWDATA = BASEPATH / "nba_data" / "raw" / "play_by_play.csv"
OUTDIR = BASEPATH / "nba_data"/ "out"
OUTDIR.mkdir(exist_ok=True)

def main():
    '''Main'''
    run_pipeline(RAWDATA)

if __name__ == "__main__":
    main()
