# -*- coding: utf-8 -*-
from halo import Halo
import textwrap

class LogProgress():
    def __init__(self, message):
        self.message = message
        self.spinner = Halo(text=message)
    def __enter__(self):
        self.spinner.start()
        return SpinLogger(self.spinner)
    def __exit__(self, type, value, traceback):
        self.spinner.stop()

def handle_multiline(string):
    if "\n" in string:
        return textwrap.indent(string, '  ')[2:]
    else:
        return string

class SpinLogger():
    def __init__(self, spinner):
        self._spinner = spinner

    def error(self, message):
        self._spinner.fail(handle_multiline(message)).start()

    def warn(self, message):
        self._spinner.warn(handle_multiline(message)).start()

    def info(self, message):
        self._spinner.info(handle_multiline(message)).start()

    def debug(self, message):
        self._spinner.stop_and_persist(symbol="🐛".encode("utf-8"), text=handle_multiline(message)).start()

    def log(self, message, symbol=" "):
        self._spinner.stop_and_persist(symbol=symbol, text=handle_multiline(message)).start()
