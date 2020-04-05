import os
import sys
import logging
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-l", "--logdir", type=str)
args = parser.parse_args(sys.argv[1:])

def get(key=None):
    if key is None:
        return _config

    return _config[key]

def _get_config():
    try:
        config = {
            "app_name": "PKG_NAME",
            "logdir": args.logdir
            # "max_process_count": int(os.environ.get("MAX_PROCESS_COUNT", 2))
        }

        # if config.get("max_process_count") > 5:
        #    raise ValueError("Invalid max_process_count!")
        
    except Exception as e:
        logging.error("Error occured: %s", str(e))
        raise e    

    return config

_config = _get_config()
