from spinlog import LogProgress
from time import sleep
import logging
import sys
from logging.handlers import RotatingFileHandler
 
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
with LogProgress("yolololo", is_spinning=should_spin, alternative_logger=stream_logger, concommitant_logger=file_logger) as s:
    sleep(2)
    s.warn("ah bon?")
    sleep(2)
    s.error("BIM\nBIM")
    sleep(2)
    s.info("HAHA\nHAHA")
    s.log("HAHA")
    s.log("HAHA", symbol="😆".encode("utf-8"))
    sleep(2)
    s.debug("HAHA oui c'est drole")
    sleep(2)

