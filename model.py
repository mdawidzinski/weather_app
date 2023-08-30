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
        self.df = None

    def get_api_data(self) -> Dict[str, Any]:
        """Method responsible for retrieving data from API"""
        response = requests.get(self.url)
        api_data = response.json()
        return api_data

    def get_excel_data(self) -> pd.DataFrame:
        """Method responsible for reading data from Excel"""
        weather_data = pd.read_excel(self.data)
        return weather_data

    def prepare_data(self) -> None:
        """Method responsible for preparing data for the graph"""
        weather_data = self.get_excel_data()

        last_row = weather_data.iloc[-1]
        last_day = last_row["Date"]

        first_day_of_last_month = last_day.replace(day=1)

        filtered_data = weather_data[weather_data['Date'].between(first_day_of_last_month, last_day)]

        self.df = filtered_data

    def find_max_value_and_date(self) -> Tuple[str, str]:
        """Method responsible for searching max value in dataframe along with date"""
        max_value_index = self.df[self.data_type].idxmax()
        data_max_value = self.df.loc[max_value_index]

        max_value = data_max_value[self.data_type]
        max_value_date = data_max_value["Date"]
        max_value_date = max_value_date.date()

        return max_value, max_value_date

    def find_min_value_and_date(self) -> Tuple[str, str]:
        """Method responsible for searching min value in dataframe along with date"""
        min_value_index = self.df[self.data_type].idxmin()
        data_min_value = self.df.loc[min_value_index]

        min_value = data_min_value[self.data_type]
        min_value_date = data_min_value["Date"]
        min_value_date = min_value_date.date()

        return min_value, min_value_date

    def calculate_average(self) -> float:
        """Method responsible for calculating average value"""
        average_value = self.df[self.data_type].mean()
        rounded_average = round(average_value, 2)

        return rounded_average

    def calculate_median(self) -> float:
        """Method responsible for calculating median value"""
        median_value = self.df[self.data_type].median()
        rounded_median = round(median_value, 2)

        return rounded_median


