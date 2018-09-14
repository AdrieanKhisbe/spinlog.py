from halo import Halo
from time import sleep

spinner = Halo(text='Loading', spinner='dots')
spinner.start()
sleep(2)
spinner.info('Yoyo')
spinner.start()
sleep(2)
spinner.stop()