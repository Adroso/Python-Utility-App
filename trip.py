__author__ = 'Adroso'

import datetime  # Used for date input checks in Details()


class Error(RuntimeError):
    """Derived from the built-in Exception class, handles errors"""

    def __init__(self, value):
        super.__init__(value)


class Country:
    """Represents a single country's details"""

    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def format_currency(self, value):
        return self.currency_symbol + (format(value, ".0f"))

    def __str__(self):
        return str(self.name + ' ' + self.currency_code + ' ' + self.currency_symbol)


class Details:
    """Records sequence of countries visited during a trip"""

    def __init__(self, country_name, start_date, end_date):
        self.locations = []
        self.country_name = country_name
        self.start_date = start_date
        self.end_date = end_date

    def add(self, country_name, start_date, end_date ):
        """Error Checking Section for add()"""

        try:      # All parameters are text
            isinstance(country_name, str)
            isinstance(start_date, str)
            isinstance(end_date, str)

        except:
            raise Error("Not Text")

        try:
            datetime.datetime.strptime(self.start_date, '%Y-%m-%d')
            datetime.datetime.strptime(self.end_date, '%Y-%m-%d')
        except:
            raise Error("Incorrect format, should be YYYY/MM/DD")

        try:
            self.start_date > self.end_date
        except:
            print('The start date is after the end date')

        self.locations.append((self.country_name, self.start_date, self.end_date))

    def current_country(self, date_string,):

        if self.start_date < date_string < self.end_date:
            return self.country_name
        else:
            return 'lol'

    def is_empty(self):
        try:
            if not self:
                 return 'Empty'
        except Error as Empty:
            print(Empty)

