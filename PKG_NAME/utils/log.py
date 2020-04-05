import logging
from pathlib import Path

from .. import conf

from .helpers import get_path_compatible_date

def setup_logger():
    root_logger = logging.getLogger()
    root_logger.setLevel("DEBUG")

    formatter = logging.Formatter(
        "%(asctime)s " + conf.get("app_name") + " %(name)-25s %(threadName)s %(levelname)-6s %(message)s")

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    root_logger.addHandler(streamHandler)
    
    if (conf.get("logdir")):
        
        log_file = Path(conf.get("logdir"), get_path_compatible_date() + ".log")
        fileHandler = logging.FileHandler(log_file)
        fileHandler.setFormatter(formatter)
        root_logger.addHandler(fileHandler)

    logging.getLogger(__name__).info("initialized logger")

setup_logger()