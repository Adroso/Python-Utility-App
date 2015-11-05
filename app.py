__author__ = 'Adroso'

from trip import Details
from trip import Error
import currency
import time
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class CurrencyConverterApp(App):

    saved_trips = []
    config_file = open("config.txt", 'r', encoding='utf-8')
    next(config_file)
    for line in config_file:
        current_line = line.split(',')
        saved_trips.append(current_line[0])

    #Constucting current date string
    current_date = time.strftime("%Y/%m/%d")
    current_date_build = 'Today is:' + '\n' + current_date

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

    current_location = details.current_country(current_date)
    current_trip = 'Current trip location:' + '\n' + details.current_country(current_date)

    application_config.close()

    def __init__(self):
        super(CurrencyConverterApp, self).__init__()

    def build(self):
        Window.size = 350, 700
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.config_check()
        self.disable_gui()
        return self.root

    def config_check(self):
        all_country_details = sorted(currency.get_all_details())
        application_config = open("config.txt", 'r', encoding='utf-8')

        #checking config file for correct data protocols
        first_line = application_config.readline()
        if first_line.strip("\n") in all_country_details:
            for line in application_config:
                if len(line.split(',')) != 3:
                    self.root.ids.app_status.text = 'Invalid Trip Details'
                    self.disable_gui()
                    break
                else:
                    self.root.ids.app_status.text = 'Trip Details Accepted'
        else:
            self.root.ids.app_status.text = 'Invalid Trip Details'
            self.disable_gui()

        application_config.close()

    def app_update(self):
        """ This function handles the update currency button """
        self.enable_gui()
        self.update_currency()
        current_time = datetime.now().strftime('%H:%M:%S')
        self.root.ids.app_status.text = 'Updated At ' + current_time

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
        self.root.ids.away_currency_input.disabled = True
        self.root.ids.away_spinner.disabled = True
        self.root.ids.home_currency_input.disabled = True
        # self.root.ids.update_currency.disabled = True

    def enable_gui(self):
        """ This Function is used on startup when the config file is incorrect"""
        self.root.ids.away_currency_input.disabled = False
        self.root.ids.away_spinner.disabled = False
        self.root.ids.home_currency_input.disabled = False
        self.root.ids.update_currency.disabled = False

    def update_currency(self):
        """This function caches a conversion rate between the selected home country and away country"""

        if self.root.ids.away_spinner.text == '':
            user_country = self.current_location
            self.root.ids.away_spinner.text = str(user_country)
            self.root.ids.home_currency_input.text = str('')

        self.cached_conversion = {}
        # for country in self.saved_trips:
        all_country_details = currency.get_all_details()

        home_country_details = all_country_details.get(self.root.ids.user_country.text.strip('\n'))
        home_currency_code = home_country_details[1]

        away_country_details = all_country_details.get(self.root.ids.away_spinner.text)
        away_currency_code = away_country_details[1]

        for country in self.saved_trips:
            country_code = all_country_details.get(country)
            current_code = country_code[1]
            current_rate = currency.convert(1, country_code[1], home_currency_code)
            self.cached_conversion[country] = current_rate
            if current_code == away_currency_code:
                pass
            else:
                current_rate = currency.convert(1, country_code[1], home_currency_code)
                self.cached_conversion[country] = current_rate


    def handle_convert(self, event_catcher):
        """handles the calculation of the conversion between rates"""
        all_country_details = currency.get_all_details()

        # extracting matching away code out of dictionary
        away_country_details = all_country_details.get(self.root.ids.away_spinner.text)
        away_currency_code = away_country_details[1]

        # extracting matching home code out of dictionary
        home_country_details = all_country_details.get(self.root.ids.user_country.text.strip('\n'))
        home_currency_code = home_country_details[1]

        #On initial startup, stops -1 being displayed in the home text box.
        if self.root.ids.away_currency_input.text == '':
            self.root.ids.home_currency_input.text = str('')

        #If the event is received from the 'away' text box
        elif event_catcher == 'away':
            cached_rate = float(self.root.ids.away_currency_input.text)

            convert_rate = self.cached_conversion[away_country_details[0]] * cached_rate
            convert_rate = "{0:.3f}".format(convert_rate)
            self.root.ids.home_currency_input.text = str(convert_rate)
            self.root.ids.app_status.text = (away_currency_code + '(' + away_country_details[2] + ') to ' + home_currency_code + '(' + home_country_details[2] +')')
        #If the event is received from the 'away' text box

        elif event_catcher == 'home':
            cached_rate = float(self.root.ids.home_currency_input.text)

            convert_rate = cached_rate / self.cached_conversion[away_country_details[0]]
            convert_rate = "{0:.3f}".format(convert_rate)
            self.root.ids.away_currency_input.text = str(convert_rate)
            self.root.ids.app_status.text = (home_currency_code + '(' + home_country_details[2] + ') to ' + away_currency_code + '(' + away_country_details[2] +')')

if __name__ == '__main__':
    CurrencyConverterApp().run()
