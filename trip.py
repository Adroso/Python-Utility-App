__author__ = 'Adroso'

import datetime  # Used for date input checks in Details()


class Error(Exception):
    """Derived from the built-in Exception class, handles errors"""

    def __init__(self, value):
        self.value = value
        super.__init__(value)


class Country:
    """Represents a single country's details"""

    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def format_currency(self, value):
        return self.currency_symbol + format(value, ".0f")

    def __str__(self):
        return str(self.name + ' ' + self.currency_code + ' ' + self.currency_symbol)


class Details:
    """Records sequence of countries visited during a trip"""

    def __init__(self, country_name, start_date, end_date):
        self.locations = []
        self.country_name = country_name
        self.start_date = start_date
        self.end_date = end_date

    def add(self):

        """Error Checking Section for add()"""
        if not isinstance(self.country_name, str) or isinstance(self.start_date, str) or isinstance(self.end_date, str):
            raise Error('Error, Input data is meant to be text')

        try:
            datetime.datetime.strptime(self.start_date, '%Y/%m/%d')
            datetime.datetime.strptime(self.end_date, '%Y/%m/%d')

        except Error as err:
            print(err)

        try:
            self.locations.__contains__(self.start_date)
        except Error as err:
            print(err)

        if self.start_date > self.end_date:
            raise Error(RuntimeError)


        self.locations.append((self.country_name, self.start_date, self.end_date))
        return self.locations

    def current_country(self, date_string, ):
        if not datetime.datetime.strptime(date_string, '%Y/%m/%d'):
            raise Error('date is not correct')

        if self.start_date < date_string < self.end_date:
            return self.country_name
        else:
            raise Error('Date is in wrong format, YYYY/MM/DD')

    def is_empty(self):
        if not self:
            return 'Empty'
        else:
            return 'Not Empty'
