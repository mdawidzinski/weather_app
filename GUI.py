from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class WeatherAppGui(QMainWindow):
    """GUI window for the YouTube downloader application."""
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        uic.loadUi("weather_app.ui", self)

