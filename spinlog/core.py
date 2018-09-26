# -*- coding: utf-8 -*-
from halo import Halo
import textwrap


class Spinner():
    def __init__(self, is_spinning=None, alternative_logger=None, concommitant_logger=None,
                 spinner=None):
        self.spinner = spinner
        self.alternative_logger = alternative_logger
        self.concommitant_logger = concommitant_logger
        self.spinning = is_spinning is None or is_spinning
    def __call__(self, message, spinner=None):
        return LogProgress(message, spinner=(spinner or self.spinner),
                           is_spinning=self.spinning,
                           alternative_logger=self.alternative_logger,
                           concommitant_logger=self.concommitant_logger)

class LogProgress():
    def __init__(self, message, spinner=None,
                 is_spinning=None, alternative_logger=None, concommitant_logger=None):
        self.message = message
        self.spinner = Halo(text=message, spinner=spinner)
        self.alternative_logger = alternative_logger
        self.concommitant_logger = concommitant_logger
        self.spinning = is_spinning is None or is_spinning

    def __enter__(self):
        if self.spinning:
            self.spinner.start()
            return SpinLogger(self.spinner, self.concommitant_logger)
        else:
            return BasicLogger(self.message, self.alternative_logger)

    def __exit__(self, type, value, traceback):
        if self.spinning:
            self.spinner.stop()


def handle_multiline(string):
    if not string:
        return string
    elif "\n" in string:
        return textwrap.indent(string, '  ')[2:]
    else:
        return string


class SpinLogger():
    def __init__(self, spinner, logger):
        self._spinner = spinner
        self._logger = logger

    def update_spinner(self, message, color=None, spinner=None):
        self._spinner.text = message
        if color: self._spinner.color = color
        if spinner: self._spinner.spinner = spinner

    def error(self, message=None):
        self._spinner.fail(handle_multiline(message)).start()
        if self._logger: self._logger.error(message or self._spinner.text)

    def warn(self, message=None):
        self._spinner.warn(handle_multiline(message)).start()
        if self._logger: self._logger.warn(message or self._spinner.text)

    def info(self, message=None):
        self._spinner.info(handle_multiline(message)).start()
        if self._logger: self._logger.info(message or self._spinner.text)

    def debug(self, message=None):
        self._spinner.stop_and_persist(symbol="🐛".encode(
            "utf-8"), text=handle_multiline(message)).start()
        if self._logger: self._logger.debug(message or self._spinner.text)

    def log(self, message=None, symbol=" "):
        self._spinner.stop_and_persist(
            symbol=symbol, text=handle_multiline(message)).start()
        if self._logger: self._logger.info((symbol.decode("utf-8") + " " 
                                           if symbol and symbol != " " else "") + 
                                           (message or self._spinner.text))


class BasicLogger():
    def __init__(self, message, logger):
        self._logger = logger
        self.message = message

    def update_spinner(self, message, color=None, spinner=None):
        self.message = message

    def error(self, message=None):
        self._logger.error(message or self.message)

    def warn(self, message=None):
        self._logger.warn(message or self.message)

    def info(self, message=None):
        self._logger.info(message or self.message)

    def debug(self, message=None):
        self._logger.debug(message or self.message)

    def log(self, message=None, symbol=""):
        self._logger.info((symbol.decode("utf-8") + " " if symbol else "") + (message or self.message))
