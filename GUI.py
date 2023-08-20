from PyQt5 import uic
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMainWindow
from datetime import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from typing import Tuple


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

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.scroll_area.setWidget(self.canvas)

        self.show_button.clicked.connect(self.show_graph)
        self.zoom_in_b.clicked.connect(self.zoom_in)
        self.zoom_out_b.clicked.connect(self.zoom_out)

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

    def zoom_in(self) -> None:
        """Allows zoom in graph"""
        ax = self.figure.gca()
        xmin, xmax = ax.get_xlim()
        x_range = xmax - xmin
        new_xmin = xmin + x_range * 0.1
        new_xmax = xmax - x_range * 0.1
        ax.set_xlim(new_xmin, new_xmax)
        self.canvas.draw()

    def zoom_out(self) -> None:
        """Allows zoom out graph"""
        ax = self.figure.gca()
        xmin, xmax = ax.get_xlim()
        x_range = xmax - xmin
        new_xmin = xmin - x_range * 0.1
        new_xmax = xmax + x_range * 0.1
        ax.set_xlim(new_xmin, new_xmax)
        self.canvas.draw()

    def get_graph_data(self) -> Tuple[str, str, str]:
        """Collect user-selected graph data from GUI"""
        graph = self.graph_combobox.currentText()
        data_type = self.data_combobox.currentText()
        period = self.period_combobox.currentText()

        return graph, data_type, period

    def show_graph(self) -> None:
        """Method responsible for graph display"""
        graph, data_type, period = self.get_graph_data()

        self.controller.set_gui_data(graph, data_type, period)

        self.controller.plot_data(self.figure, self.canvas)

        self.zoom_out_b.setEnabled(True)
        self.zoom_in_b.setEnabled(True)
