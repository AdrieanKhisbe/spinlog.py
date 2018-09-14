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

    def log(self, message):
        self._spinner.info(message).start()

    def debug(self, message):
        self._spinner.clear()
        print(f"DEBUG {message}")
        self._spinner.start()
