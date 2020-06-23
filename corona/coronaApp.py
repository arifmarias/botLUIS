from covid import Covid
import pyowm
from config.config_reader import ConfigReader

class CoronaInformation():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        

    def get_corona_info(self,city):
        self.city=city
        covid = Covid()
        cases = covid.get_status_by_country_name(city)
        d = str(cases['deaths'])
        self.bot_says = "Total Death " + d 
        return self.bot_says