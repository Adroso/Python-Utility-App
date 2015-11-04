__author__ = 'Adroso'

class Error(Exception):
    """Derived from the built-in Exception class, handles errors"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Country:
    """Represents a single country's details"""

    def __init__(self, name, code, symbol):
        self.name = name
        self.code = code
        self.symbol = symbol

    def format_currency(self, amount):
        return self.symbol + str(round(amount, 2))

    def __str__(self):
        return '{} ({})'.format(self.name, self.code)

    @classmethod
    def make(cls, data_list):
        if not data_list:
            raise Error("can't make country")
        return Country(*data_list)


class Details:
    """Records sequence of countries visited during a trip"""

    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        if start_date > end_date:
            raise Error('invalid trip dates: {} {}'.format(start_date, end_date))
        for location in self.locations:
            if location[0] == start_date:
                raise Error('{}-{} already added'.format(start_date, end_date))
        self.locations.append((start_date, end_date, country_name))

    def current_country(self, date_string):
        for location in self.locations:
            if location[0] <= date_string <= location[1]:
                return location[2]
        raise Error('invalid date')

    def is_empty(self):
        if len(self.locations) == 0:
            return True  # Empty locations
        else:
            return False  # values in locations


if __name__ == '__main__':
    from currency import get_details
    import time

    print('test country class')
    country = Country('Australia', 'AUD', '$')
    print(country.format_currency(10.95))
    country = Country.make(get_details("Turkey"))
    print(country.format_currency(10.95))

    print('test tripdetails class')
    trip = Details()
    trip.add(country, "2015/09/05", "2015/09/20")
    trip.add(country, "2015/09/21", "2016/09/20")
    try:
        print(trip.current_country("2015/09/01"))
    except Error as error:
        print(error.value)

    print(trip.current_country(time.strftime('%Y/%m/%d')))

    try:
        trip.add(country, "2015/09/05", "2015/09/20")
    except Error as error:
        print(error.value)


# loop_check = True
#     while loop_check:
#         name = str(input('Country Name:'))
#         code = str(input('Currency Code:'))
#         symbol = str(input('Currency Symbol:'))
#         amount = int(input('Enter Amount:'))
#
#         object_input = Country(name, code, symbol)
#         currency_format = object_input.format_currency(amount)
#         string_check = str(object_input)
#
#         print('Formatted Currency for', name, 'of amount', amount, ':', currency_format)
#         print('__str__ method produces:', string_check)
#
#         loop_check = input('check again or move on to next check? Y or N').upper()
#         if loop_check == 'Y':
#             loop_check = True
#         else:
#             loop_check = False
#
#     loop_check = True
#     while loop_check:
#         name = str(input('Country Name:'))
#         startDate = str(input('Trip Start date:'))
#         endDate = str(input('Trip End date:'))
#
#         object_input = Details(name, startDate, endDate)
#         add_test = object_input.add(object_input)
#         """Checking all error checking"""
#
#         dateString = input('Now check current_country by entering a date between the trip:')
#         currentCountry = object_input.current_country(dateString)
#
#         loop_check = input('check again? Y or N').upper()
#         if loop_check == 'Y':
#             loop_check = True
#         else:
#             loop_check = False
