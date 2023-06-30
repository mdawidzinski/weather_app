import requests
import pandas as pd


class CurrentWeatherModel:
    def __init__(self, data):
        self.url = "https://danepubliczne.imgw.pl/api/data/synop/station/wroclaw"
        self.data = data

    def get_api_data(self):
        response = requests.get(self.url)
        api_data = response.json()
        return api_data

    def get_excel_data(self):
        weather_data = pd.read_excel(self.data)
        return weather_data

    def get_avg_temp(self):
        weather_data = self.get_excel_data()

        target_date = pd.Timestamp(year=pd.Timestamp.today().year, month=pd.Timestamp.today().month,
                                   day=pd.Timestamp.today().day)

        df_previous_years = weather_data[(weather_data['date'].dt.month == target_date.month) &
                                         (weather_data['date'].dt.day == target_date.day) &
                                         (weather_data['date'].dt.year < target_date.year)]

        avg_temp = df_previous_years['tavg'].mean()
        return avg_temp
