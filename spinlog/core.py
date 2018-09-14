# -*- coding: utf-8 -*-
from halo import Halo


class LogProgress():
    def __init__(self, message):
        self.message = message
        self.spinner = Halo(text=message)
    def __enter__(self):
        self.spinner.start()
        return SpinLogger(self.spinner)
    def __exit__(self, type, value, traceback):
        self.spinner.stop()



class SpinLogger():
    def __init__(self, spinner):
        self._spinner = spinner

    def error(self, message):
        self._spinner.fail(message).start()

    def warn(self, message):
        self._spinner.warn(message).start()

    def info(self, message):
        self._spinner.info(message).start()

    def debug(self, message):
        self._spinner.stop_and_persist(symbol="🐛".encode("utf-8"), text=message).start()

    def log(self, message, symbol=" "):
        self._spinner.stop_and_persist(symbol=symbol, text=message).start()
