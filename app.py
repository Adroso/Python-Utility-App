__author__ = 'Adroso'

from trip import Details
from trip import Error
import currency
import time
import datetime
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
# from kivy.properties import ObjectProperty
from kivy.core.window import Window
# from kivy.properties import StringProperty
# from kivy.properties import ListProperty
# from kivy.graphics import Color


class CurrencyConverterApp(App):

    # countries_spinner = StringProperty()
    # saved_trips = ListProperty()

    saved_trips = []
    config_file = open("config.txt", 'r', encoding='utf-8')
    next(config_file)
    for line in config_file:
        current_line = line.split(',')
        saved_trips.append(current_line[0])


    #Constucting current date string
    current_date = time.strftime("%Y/%m/%d")
    current_date_build = 'Today is:' + ' ' + current_date

    #Getting and constructing home country
    application_config = open("config.txt", 'r', encoding='utf-8')
    home_country = application_config.readline()

    #current trip
    next(application_config)
    details = Details()
    for line in application_config:
        user_trip = line.split(",")
        try:
            details.add(user_trip[0], user_trip[1], user_trip[2])
        except Error as err:
            print(err)

    current_trip = 'Current trip location:' + ' ' + details.current_country(current_date)

    application_config.close()

    def __init__(self):
        super(CurrencyConverterApp, self).__init__()

    def build(self):
        Window.size = 350, 700
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.config_check()


        return self.root

    def config_check(self):
        all_country_details = sorted(currency.get_all_details())
        application_config = open("config.txt", 'r', encoding='utf-8')

        #checking config file for correct data protocols
        first_line = application_config.readline()
        if first_line.strip("\n") in all_country_details:
            for line in application_config:
                if len(line.split(',')) != 3:
                    self.disable_gui()

                    break
                else:
                    # self.root.ids.app_status.text = 'invalid trip details'
                    self.root.ids.app_status.text = 'trip details accepted'
        else:
            self.disable_gui()

        application_config.close()

    def app_update(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.root.ids.app_status.text = 'updated at ' + current_time

    # def countries_spinner(self,):
    #     """ handle change of spinner selection, output result to label widget """
    #     saved_trips = []
    #     config_file = open("config.txt", 'r', encoding='utf-8')
    #     next(config_file)
    #     for line in config_file:
    #         current_line = line.split(',')
    #         saved_trips.append(current_line[0])
    #     return saved_trips

    def disable_gui(self):
        """ This Function is used on startup when the config file is incorrect"""
        self.root.ids.app_status.text = 'invalid trip details'
        self.root.ids.away_currency_input.disabled = True
        self.root.ids.away_spinner.disabled = True
        self.root.ids.home_currency_input.disabled = True
        self.root.ids.update_currency.disabled = True

    def handle_convert(self):

        """handles the calculation of the conversion between rates"""
        all_country_details = currency.get_all_details()


        # extracting matching away code out of dictionary
        away_country_details = all_country_details.get(self.root.ids.away_spinner.text)
        away_currency_code = away_country_details[1]

        # extracting matching home code out of dictionary
        home_country_details = all_country_details.get(self.root.ids.user_country.text.strip('\n'))
        home_currency_code = home_country_details[1]


        convert_rate = currency.convert(self.root.ids.away_currency_input.text,away_currency_code,home_currency_code)
        self.root.ids.home_currency_input.text = str(convert_rate)
        self.root.ids.app_status.text = (away_currency_code + '(' + away_country_details[2] + ') to ' + home_currency_code + '(' + home_country_details[2] +')')



if __name__ == '__main__':
    CurrencyConverterApp().run()
