__author__ = 'Adroso'

import datetime #Used for date input checks in Details()



class Error(RuntimeError):
    """Derived from the built-in Exception class, handles errors"""
    def __init__(self, value):
        self.value = value
        super.__init__(value)






class Country:

    """Represents a single country's details"""
    def __init__(self, name, currency_code, currency_symbol ):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol


    def format_currency(self, value):
        return self.currency_symbol + (format(value, ".0f"))

    def __str__(self):
        return str(self.name + ' ' + self.currency_code + ' ' + self.currency_symbol)






class Details:
    """Records sequence of countries visited during a trip"""
    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):

        try:
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except:
            raise Error("Incorrect format, should be YYYY/MM/DD")

        try:
            start_date > end_date
        except:
            print('The start date is after the end date')

        self.locations.append((country_name, start_date, end_date))

    def current_country(self, date_string, country_name, start_date, end_date ):

        if  start_date < date_string < end_date:
            return country_name
        else:
            return 'lol'

    def is_empty(self):
        if not self:
            return 'Empty'
        else:
            return 'Not Empty'

