from PyQt5 import uic
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMainWindow
from datetime import datetime


class WeatherAppGui(QMainWindow):
    """GUI window for the YouTube downloader application."""
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        uic.loadUi("weather_app.ui", self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)  # refresh timer every 1 second

        self.update_gui_from_api()
        self.update_date_time()

        self.zoom_in_b.clicked.connect(self.zoom_in)
        self.zoom_out_b.clicked.connect(self.zoom_out())

    def update_gui_from_api(self) -> None:
        """Update GUI with the data from API"""
        city, temperature, pressure, humidity, wind = self.controller.prepare_weather_data()

        symbol = "\u00b0"
        self.city_label.setText(city)
        self.temperature_label.setText(f"Temperature: {temperature}{symbol}C")
        self.pressure_label.setText(f"Pressure: {pressure} hPa")
        self.humidity_label.setText(f"Humidity: {humidity}%")
        self.wind_label.setText(f"Wind: {wind} km/h")

    def update_date_time(self) -> None:
        """Update GUI with date and time"""
        today = datetime.now().strftime("%d. %B %Y")
        current_time = QTime.currentTime()

        self.date_label.setText(today)
        self.time_label.setText(current_time.toString("hh:mm:ss"))

    def zoom_in(self):
        """Allows zoom in graph"""
        ax = self.figure.gca()
        ax.set_xlim(ax.get_xlim()[0] * 0.9, ax.get_xlim()[1] * 0.9)
        self.canvas.draw()

    def zoom_out(self):
        """Allows zoom in graph"""
        ax = self.figure.gca()
        ax.set_xlim(ax.get_xlim()[0] * 1.1, ax.get_xlim()[1] * 1.1)
        self.canvas.draw()
