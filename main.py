from spinlog import LogProgress
from time import sleep

with LogProgress("yolololo") as s:
    sleep(2)
    s.log("HAHA")
    sleep(2)
