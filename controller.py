class CurrentWeatherController:
    def __init__(self, model):
        self.model = model

    def prepare_weather_data(self):
        """Method responsible for preparing data from API to display in GUI"""
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

    def set_gui_data(self, graph, data_type, period):
        """Method responsible for send information about graph form GUI to model"""
        self.model.graph = graph
        self.model.data_type = data_type
        self.model.period = period

    def plot_data(self, figure, canvas):
        """Method responsible for generating graph using data from model"""
        data, data_type = self.model.prepare_data()

        figure.clear()
        ax = figure.add_subplot(111)

        x = data['date']
        y = data[data_type]

        ax.plot(x, y, marker='o')
        ax.set_xlabel('Date')
        ax.set_ylabel(data_type)
        ax.set_title(f'{data_type} Over Time')
        ax.tick_params(axis='x', rotation=45)

        figure.subplots_adjust(left=0.1, bottom=0.24, right=0.97, top=0.9)

        return canvas.draw()
