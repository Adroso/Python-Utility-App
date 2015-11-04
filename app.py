__author__ = 'Adroso'

from trip import Details
from trip import Error
import currency
import time
import datetime
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.graphics import Color



class CurrencyConverterApp(App):

    countries_spinner = StringProperty()
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
        # application_config = open("config.txt", 'r', encoding='utf-8')
        #
        # #checking config file for correct data protocols
        # first_line = application_config.readline()
        # if first_line == '' or len(first_line.split()) > 2:
        #     self.root.ids.app_status.text = 'invalid trip details'
        # else:
        #     self.root.ids.app_status.text = 'trip details loaded'
        # # Applies to lines after the header line
        # for line in application_config:
        #     if len(line.split(',')) >3:
        #         self.root.ids.app_status.text = 'invalid trip details'
        #     else:
        #         self.root.ids.app_status.text = 'trip details loaded'
        #
        # application_config.close()

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
                print(len(line.split(',')))
                if len(line.split(',')) != 3:
                    self.root.ids.app_status.text = 'invalid trip details'
                    break
                else:
                    self.root.ids.app_status.text = 'invalid trip details'

                    self.root.ids.app_status.text = 'trip details accepted'
        else:
            self.root.ids.app_status.text = 'invalid trip details'
        # else:
        #     for line in application_config:
        #         if len(line.split(',')) >3:
        #             self.root.ids.app_status.text = 'invalid trip details'
        #         else:
        #             self.root.ids.app_status.text = 'trip details loaded successfully'

        # Applies to lines after the header line
        # for line in application_config:
        #     if len(line.split(',')) >3:
        #         self.root.ids.app_status.text = 'invalid trip details'
        #     else:
        #         self.root.ids.app_status.text = 'trip details loaded successfully'

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


    def handle_convert(self):
        """handles the calculation of the conversion between rates"""


if __name__ == '__main__':
    CurrencyConverterApp().run()
