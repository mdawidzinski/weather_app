from datetime import datetime


class CurrentWeatherController:
    def __init__(self, model):
        self.model = model

    def prepare_weather_data(self):
        city = ""
        temperature = ""
        pressure = ""
        humidity = ""
        wind = ""

        data = self.model.get_api_data()

        for key, value in data.items():
            if key == "stacja":
                city = value
            elif key == "temperatura":
                temperature = value
            elif key == "cisnienie":
                pressure = value
            elif key == "predkosc_wiatru":
                wind = value
            elif key == "wilgotnosc_wzgledna":
                humidity = value

        return city, temperature, pressure, humidity, wind

    def prepare_data(self):
        location, temperature, pressure, = self.prepare_weather_data()
        current_time = self.prepare_time_data().strftime('%H:%M:%S')
        avg_temp = self.prepare_avg_data()
        return location, temperature, pressure, current_time, avg_temp

    def prepare_time_data(self):
        return datetime.now().time()

    def prepare_avg_data(self):
        return self.model.get_avg_temp()
