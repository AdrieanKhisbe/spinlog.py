from halo import Halo

class LogProgress():
    def __init__(self, message):
        self.message = message
        self.spinner = Halo(text=message)
    def __enter__(self):
        self.spinner.start()
    def __exit__(self, type, value, traceback):
        self.spinner.stop()
