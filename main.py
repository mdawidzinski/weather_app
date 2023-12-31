from GUI import WeatherAppGui
from controller import CurrentWeatherController
from model import CurrentWeatherModel
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = CurrentWeatherModel('weather_data.xlsx')
    controller = CurrentWeatherController(model)
    view = WeatherAppGui(controller)
    view.show()
    sys.exit(app.exec_())
