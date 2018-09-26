# -*- coding: utf-8 -*-
from halo import Halo
import textwrap


class LogProgress():
    def __init__(self, message,
                 is_spinning=None, alternative_logger=None, concommitant_logger=None):
        self.message = message
        self.spinner = Halo(text=message)
        self.alternative_logger = alternative_logger
        self.concommitant_logger = concommitant_logger
        self.spinning = is_spinning is None or is_spinning
        print(is_spinning, self.spinning)

    def __enter__(self):
        if self.spinning:
            self.spinner.start()
            return SpinLogger(self.spinner, self.concommitant_logger)
        else:
            return BasicLogger(self.alternative_logger)

    def __exit__(self, type, value, traceback):
        if self.spinning:
            self.spinner.stop()


def handle_multiline(string):
    if "\n" in string:
        return textwrap.indent(string, '  ')[2:]
    else:
        return string


class SpinLogger():
    def __init__(self, spinner, logger):
        self._spinner = spinner
        self._logger = logger

    def error(self, message):
        self._spinner.fail(handle_multiline(message)).start()
        if self._logger: self._logger.error(message)

    def warn(self, message):
        self._spinner.warn(handle_multiline(message)).start()
        if self._logger: self._logger.warn(message)

    def info(self, message):
        self._spinner.info(handle_multiline(message)).start()
        if self._logger: self._logger.info(message)

    def debug(self, message):
        self._spinner.stop_and_persist(symbol="🐛".encode(
            "utf-8"), text=handle_multiline(message)).start()
        if self._logger: self._logger.debug(message)

    def log(self, message, symbol=" "):
        self._spinner.stop_and_persist(
            symbol=symbol, text=handle_multiline(message)).start()
        if self._logger: self._logger.info((symbol.decode("utf-8") + " " if symbol and symbol != " " else "") + message)


class BasicLogger():
    def __init__(self, logger):
        self._logger = logger

    def error(self, message):
        self._logger.error(message)

    def warn(self, message):
        self._logger.warn(message)

    def info(self, message):
        self._logger.info(message)

    def debug(self, message):
        self._logger.debug(message)

    def log(self, message, symbol=""):
        self._logger.info((symbol.decode("utf-8") + " " if symbol else "") + message)
