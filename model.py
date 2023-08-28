import requests
import pandas as pd
from pathlib import Path
from typing import Dict, Any, Tuple

class CurrentWeatherModel:
    def __init__(self, data: Path):
        self.url = "https://danepubliczne.imgw.pl/api/data/synop/station/wroclaw"
        self.data = data
        self.graph = ""
        self.data_type = ""
        self.period = ""

    def get_api_data(self) -> Dict[str, Any]:
        """Method responsible for retrieving data from API"""
        response = requests.get(self.url)
        api_data = response.json()
        return api_data

    def get_excel_data(self) -> pd.DataFrame:
        """Method responsible for reading data from Excel"""
        weather_data = pd.read_excel(self.data)
        return weather_data

    def prepare_data(self) -> Tuple[pd.DataFrame, str]:
        """Method responsible for preparing data for the graph"""
        weather_data = self.get_excel_data()

        last_row = weather_data.iloc[-1]
        last_day = last_row["Date"]

        first_day_of_last_month = last_day.replace(day=1)

        filtered_data = weather_data[weather_data['Date'].between(first_day_of_last_month, last_day)]

        return filtered_data, self.data_type
