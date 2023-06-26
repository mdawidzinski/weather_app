from datetime import datetime


class CurrentWeatherController:
    def __init__(self, model):
        self.model = model

    def prepare_weather_data(self):
        city = ''
        temperature = ''
        pressure = ''

        data = self.model.get_data()

        for key, value in data.items():
            if key == 'stacja':
                city = value
            elif key == 'temperatura':
                temperature = value
            elif key == 'cisnienie':
                pressure = value

        return city, temperature, pressure

    def prepare_data(self):
        location, temperature, pressure, = self.prepare_weather_data()
        current_time = self.prepare_time_data().strftime('%H:%M:%S')
        return location, temperature, pressure, current_time

    def prepare_time_data(self):
        return datetime.now().time()
