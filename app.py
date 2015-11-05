__author__ = 'Adroso'

import currency
import time
from trip import Details
from trip import Error
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class CurrencyConverterApp(App):
    def __init__(self):
        super(CurrencyConverterApp, self).__init__()
        self.cached_conversion = {}  # recommended by Pycharm

    def build(self):
        Window.size = 350, 700
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.config_check()
        error_check = False
        self.disable_gui(error_check)
        return self.root

    @staticmethod  # recommended by Pycharm
    def config_trips():
        """ This function builds a list to be displayed in the spinner of the GUI"""
        saved_trips = []
        config_file = open("config.txt", 'r', encoding='utf-8')
        next(config_file)
        for line in config_file:
            current_line = line.split(',')
            saved_trips.append(current_line[0])
        return saved_trips

    @staticmethod  # recommended by Pycharm
    def current_date_build():
        """ gets current date via the devices date """
        current_date = time.strftime("%Y/%m/%d")
        return 'Today is:' + '\n' + current_date

    @staticmethod  # recommended by Pycharm
    def home_country():
        """ reads the first line of the config file which is assumed as the home country """
        application_config = open("config.txt", 'r', encoding='utf-8')
        return application_config.readline()

    """ global use for current date and location, NOTE: ran into errors when placed in function"""
    current_date = time.strftime("%Y/%m/%d")
    application_config = open("config.txt", 'r', encoding='utf-8')
    next(application_config)
    details = Details()
    for line in application_config:
        user_trip = line.split(",")
        try:
            details.add(user_trip[0], user_trip[1], user_trip[2])
        except Error as err:
            print(err)

    current_location = details.current_country(current_date)
    current_trip = 'Current Trip Location:' + '\n' + details.current_country(current_date)

    application_config.close()

    def config_check(self):
        """This function checks the config file for any protocol errors and if so controls the kivy gui"""
        all_country_details = sorted(currency.get_all_details())
        application_config = open("config.txt", 'r', encoding='utf-8')

        first_line = application_config.readline()
        if first_line.strip("\n") in all_country_details:
            for line in application_config:
                if len(line.split(',')) != 3:
                    self.root.ids.app_status.text = 'Invalid Trip Details'
                    error_check = True
                    self.disable_gui(error_check)
                    break
                elif line.split(',')[0] not in all_country_details:
                    self.root.ids.app_status.text = 'Invalid Trip Details'
                    error_check = True
                    self.disable_gui(error_check)
                    break
                else:
                    self.root.ids.app_status.text = 'Trip Details Accepted'
        else:
            self.root.ids.app_status.text = 'Invalid Trip Details'
            error_check = True
            self.disable_gui(error_check)

        application_config.close()

    def app_update(self):
        """ This function handles the update currency button """
        self.enable_gui()
        self.update_currency()
        current_time = datetime.now().strftime('%H:%M:%S')
        self.root.ids.app_status.text = 'Updated At ' + current_time

    def disable_gui(self, error_check):
        """ This Function is used on startup when the config file is incorrect and on startup"""
        self.root.ids.away_currency_input.disabled = True
        self.root.ids.home_currency_input.disabled = True
        if error_check:  # Occurs only when the disable GUI is because of an error
            self.root.ids.update_currency.disabled = True
            self.root.ids.away_spinner.disabled = True

    def enable_gui(self):
        """ This Function is used on startup or to enable a disabled GUI"""
        self.root.ids.away_currency_input.disabled = False
        self.root.ids.away_spinner.disabled = False
        self.root.ids.home_currency_input.disabled = False
        self.root.ids.update_currency.disabled = False

    def update_currency(self):
        """This function caches a conversion rate between all the trip countries

        The Application will use this entire cached dictionary to convert without having to connect
        - Recommended Way by Trevor
        """
        try:
            if self.root.ids.away_spinner.text == '':
                user_country = self.current_location
                self.root.ids.away_spinner.text = str(user_country)
                self.root.ids.home_currency_input.text = str('')

            all_country_details = currency.get_all_details()

            home_country_details = all_country_details.get(self.root.ids.user_country.text.strip('\n'))
            home_currency_code = home_country_details[1]

            away_country_details = all_country_details.get(self.root.ids.away_spinner.text)
            away_currency_code = away_country_details[1]

            for country in self.config_trips():
                country_code = all_country_details.get(country)
                current_code = country_code[1]
                current_rate = currency.convert(1, country_code[1], home_currency_code)
                self.cached_conversion[country] = current_rate
                if current_code == away_currency_code:
                    pass
                else:
                    current_rate = currency.convert(1, country_code[1], home_currency_code)
                    self.cached_conversion[country] = current_rate
        except Error:  # Disables the UI if update_currency fails
            self.root.ids.app_status.text = 'Failed Currency Update'
            error_check = True
            self.disable_gui(error_check)

    def handle_convert(self, event_catcher):
        """ handles the calculation of the conversion between rates with the cached conversion rates"""
        all_country_details = currency.get_all_details()

        # extracting matching away code out of dictionary
        away_country_details = all_country_details.get(self.root.ids.away_spinner.text)
        away_currency_code = away_country_details[1]

        # extracting matching home code out of dictionary
        home_country_details = all_country_details.get(self.root.ids.user_country.text.strip('\n'))
        home_currency_code = home_country_details[1]

        # On initial startup, stops -1 being displayed in the home text box.
        if self.root.ids.away_currency_input.text == '':
            self.root.ids.home_currency_input.text = str('')

        # If the event is received from the 'away' text box
        elif event_catcher == 'away':
            cached_rate = float(self.root.ids.away_currency_input.text)

            convert_rate = self.cached_conversion[away_country_details[0]] * cached_rate
            convert_rate = "{0:.3f}".format(convert_rate)
            self.root.ids.home_currency_input.text = str(convert_rate)
            self.root.ids.app_status.text = str(away_currency_code + '(' + str(away_country_details[2]).strip(
                '\n') + ') to ' + home_currency_code + '(' + str(home_country_details[2]).strip('\n') + ')')
            self.focus_check = True

        # If the event is received from the 'home' text box
        elif event_catcher == 'home':
            cached_rate = float(self.root.ids.home_currency_input.text)

            convert_rate = cached_rate / self.cached_conversion[away_country_details[0]]
            convert_rate = "{0:.3f}".format(convert_rate)
            self.root.ids.away_currency_input.text = str(convert_rate)
            self.root.ids.app_status.text = str(home_currency_code + '(' + str(home_country_details[2]).strip(
                '\n') + ') to ' + away_currency_code + '(' + (away_country_details[2]).strip('\n') + ')')
            self.focus_check = True

    focus_check = False

    def on_focus(self, value):
        """ This function clears the status message when user starts typing and handles is correct operation """
        if value:
            # print(self.lol)
            if not self.focus_check:
                self.root.ids.app_status.text = ''
                # print('im working')
            else:
                self.focus_check = False
        return


if __name__ == '__main__':
    CurrencyConverterApp().run()
