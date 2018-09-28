#!/usr/bin/env python
# When cloning the project, to be run with 'pipenv run python examples/with_logger.py'
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
## ^^ Do not use code up when installing library ^^

from spinlog import Spinner
from time import sleep
import logging
import sys
from logging.handlers import RotatingFileHandler
 

# Set up two logger
file_logger = logging.getLogger("file")
file_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
file_handler = RotatingFileHandler('spinning.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)
 
stream_logger = logging.getLogger("stream")
stream_logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_logger.addHandler(stream_handler)

should_spin = "--no-spin" not in sys.argv
print(f"Demo {'with' if should_spin else 'without'} spinner")
# Configure spinner
spinner = Spinner(spinner="triangle", is_spinning=should_spin,
                  alternative_logger=stream_logger, concommitant_logger=file_logger)

with spinner("test 1") as s:
    sleep(2)
    s.warn("ah bon?")
    sleep(2)
    s.error("BIM\nBIM")
    s.update_spinner("BAAAAM")
    sleep(2)
    s.info("HAHA\nHAHA")

# This spinner would use the same config
with spinner("test 2", spinner="circle") as s:
    s.log("BOUH")
    sleep(1)
    s.update_spinner("Ha Ha Ha", color="yellow")
    s.log("HAHA", symbol="😆".encode("utf-8"))
    sleep(2)
    s.debug("HAHA oui c'est drole")
    s.info()
    sleep(2)

