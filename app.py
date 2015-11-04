__author__ = 'Adroso'

from trip import Details
from trip import Error
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.graphics import Color


class CurrencyConverterApp(App):
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
        application_config = open("config.txt", 'r', encoding='utf-8')

        #checking config file for correct data protocols
        first_line = application_config.readline()
        if first_line == '' or len(first_line.split()) > 1:
            print('More Than 1 Word')
        else:
            print(first_line)
        # Applies to lines after the header line
        for line in application_config:
            if len(line.split(',')) >3:
                print('Nup')
            else:
                print('Yup')
        application_config.close()

    def build(self):
        Window.size = 350, 700
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')

        return self.root

    def handle_convert(self):
        """handles the calculation of the conversion between rates"""


if __name__ == '__main__':
    CurrencyConverterApp().run()
