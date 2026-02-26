import logging
from pathlib import Path

def set_up_logs():
    
    log_dir = Path(__file__).resolve().parent
    
    log_file = log_dir / "logs.log"
    
    logging.basicConfig(filename=str(log_file), 
                        filemode='a',
                        level=logging.INFO,
                        format='%(asctime)s- %(message)s')