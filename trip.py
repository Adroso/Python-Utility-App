__author__ = 'Adroso'



class Error(Exception):
    """Derived from the built-in Exception class, handles errors"""
    def __init__(self, value):
        super.__init__(value)


class Country:

    """Represents a single country's details"""
    def __init__Country(self, name, currency_code, currency_symbol ):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol


    def format_currency(value, currency_symbol):
        return currency_symbol + format(value, ".2f")

    def __str__(self, name, currency_code, currency_symbol ):
        return name + currency_code + currency_symbol

class Details:
    """Records sequence of countries visited during a trip"""
    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        import datetime

        try:
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except:
            raise Error("Incorrect data format, should be YYYY/MM/DD")

        self.locations.append((country_name, start_date, end_date))


    def is_empty(self):
        return -1






