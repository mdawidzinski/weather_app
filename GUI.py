from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class WeatherView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle('Weather App')
        self.layout = QGridLayout()
        self.label_location = QLabel()
        self.label_temperature = QLabel()
        self.label_pressure = QLabel()
        self.label_datetime = QLabel()
        self.info_label = QLabel()
        self.label_average_temperature = QLabel()
        self.setup_ui()

        self.set_up_data()

    def setup_ui(self):
        self.layout.addWidget(self.label_location, 0, 0)
        self.layout.addWidget(self.label_temperature, 0, 1)
        self.layout.addWidget(self.label_pressure, 0, 2)
        self.layout.addWidget(self.label_datetime, 0, 3)
        self.layout.addWidget(self.info_label, 1, 0)
        self.layout.addWidget(self.label_average_temperature, 1, 1)
        self.setLayout(self.layout)

    def update_weather_data(self, location, temperature, pressure, current_time, avg_temp):
        self.label_location.setText(f'City: {location}')
        self.label_datetime.setText(f'Current time: {current_time}')
        self.label_temperature.setText(f'Temperature: {temperature}')
        self.label_pressure.setText(f'Pressure: {pressure}')
        self.info_label.setText(f'Last 2 years avg:')
        self.label_average_temperature.setText(f'Temperature: {avg_temp}')

    def set_up_data(self):
        location, temperature, pressure, current_time, avg_temp = self.controller.prepare_data()
        self.update_weather_data(location, temperature, pressure, current_time, avg_temp)
