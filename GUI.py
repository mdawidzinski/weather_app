from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class WeatherView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle('Weather App')
        self.layout = QVBoxLayout()
        self.label_location = QLabel()
        self.label_datetime = QLabel()
        self.label_temperature = QLabel()
        self.label_pressure = QLabel()
        self.setup_ui()

        self.set_up_data()

    def setup_ui(self):
        self.layout.addWidget(self.label_location)
        self.layout.addWidget(self.label_datetime)
        self.layout.addWidget(self.label_temperature)
        self.layout.addWidget(self.label_pressure)
        self.setLayout(self.layout)

    def update_weather_data(self, location, temperature, pressure, current_time):
        self.label_location.setText(f'City: {location}')
        self.label_datetime.setText(f'Current time: {current_time}')
        self.label_temperature.setText(f'Temperature: {temperature}')
        self.label_pressure.setText(f'Pressure: {pressure}')

    def set_up_data(self):
        location, temperature, pressure, current_time = self.controller.prepare_data()
        self.update_weather_data(location, temperature, pressure, current_time)
