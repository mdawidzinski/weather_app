import pandas as pd


class DataMerge:
    """Merge xlsx data files into one xlsx file and prepare it for use by Weather App"""
    def __init__(self, files_to_merge: list, file_name: str = "Merged_Files"):
        self.files_to_merge = files_to_merge
        self.file_name = file_name
        self.df = None

        try:
            self.load_and_concat()
            self.drop_columns()
            self.rename_columns()
            self.convert_to_numeric()
            self.convert_to_date()
            self.save_df_to_xlsx()
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_and_concat(self) -> None:
        """Load xlsx files and merge them"""
        try:
            dfs = [pd.read_excel(file) for file in self.files_to_merge]
            self.df = pd.concat(dfs)
        except Exception as e:
            raise Exception(f"Error occurred during loading or concatenating files: {e}")

    def drop_columns(self) -> None:
        """Drop unnecessary columns"""
        column_to_drop = ["tmin", "tmax", "snow", "wdir", "wpgt", "tsun"]
        try:
            self.df = self.df.drop(columns=column_to_drop)
        except Exception as e:
            raise Exception(f"Error occurred during dropping columns file: {e}")

    def rename_columns(self) -> None:
        """Rename columns"""
        column_to_rename = {"date": "Date", "tavg": "Temperature", "prcp": "Precipitation", "wspd": "Wind speed",
                            "pres": "Pressure"}
        try:
            self.df = self.df.rename(columns=column_to_rename)
        except Exception as e:
            raise Exception(f"Error occurred during renaming columns: {e}")

    def convert_to_numeric(self) -> None:
        """Convert data to numerical values"""
        convert_to_numeric = ["Temperature", "Precipitation", "Wind speed", "Pressure"]
        try:
            for data in convert_to_numeric:
                self.df[data] = pd.to_numeric(self.df[data])
        except Exception as e:
            raise Exception(f"Error occurred during converting columns to numeric: {e}")

    def convert_to_date(self):
        """Convert Date column to date"""
        try:
            self.df["Date"] = pd.to_datetime(self.df["Date"]).dt.date
        except Exception as e:
            raise Exception(f"Error occurred during converting Date to date type: {e}")

    def save_df_to_xlsx(self) -> None:
        """Save dataframe to xlsx"""
        try:
            self.df.to_excel(self.file_name + ".xlsx", index=False)
        except Exception as e:
            raise Exception(f"Error occurred during saving file: {e}")


if __name__ == "__main__":
    files_to_merge = ['2020.xlsx', '2021.xlsx', '2022.xlsx', '2023.xlsx']
    merge = DataMerge(files_to_merge, "weather_data")

