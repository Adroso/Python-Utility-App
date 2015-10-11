__author__ = 'Adroso'

import datetime  # Used for date input checks in Details()


class Error(Exception):
    """Derived from the built-in Exception class, handles errors"""

    def __init__(self, value):
        super().__init__(value)


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

    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):

        """Error Checking Section for add()"""
        if not (isinstance(country_name, str) or isinstance(start_date, str) or isinstance(end_date, str)):
            raise Error('Error, Input data is meant to be text')

        if not str(datetime.datetime.strptime(start_date, '%Y/%m/%d') and not str(datetime.datetime.strptime(
                end_date, '%Y/%m/%d'))):
            raise Error('Wrong date format, YYYY/MM/DD')

        for location in self.locations:
            if start_date in location[1]:
                raise Error('There is a duplicate start date')

        if start_date > end_date:
            raise Error('Start Date is after End Date')

        self.locations.append((country_name, start_date, end_date))
        return self.locations

    def current_country(self, date_string):
        if not datetime.datetime.strptime(date_string, '%Y/%m/%d'):
            raise Error('date is not correct')


        for location in self.locations:
            # date_input = datetime.datetime.strptime(date_string, '%Y/%m/%d').date()
            # initial_date = datetime.datetime.strptime(location[1], '%Y/%m/%d').date()
            # final_date = datetime.datetime.strptime(location[2], '%Y/%m/%d').date()

            if (datetime.datetime.strptime(location[1], '%Y/%m/%d').date() < datetime.datetime.strptime(date_string, '%Y/%m/%d').date() < datetime.datetime.strptime(location[2], '%Y/%m/%d').date()) in self.locations:

                return location[0]
            else:
                raise Error('lol no trips')


    def is_empty(self):
        if len(self.locations) == 0:
            return True  # Empty
        else:
            return False  # Something there


""" Module Testing"""
if __name__ == "__main__":
    details = Details()
    details.add('Australia', '2018/08/12', '2100/08/12')
    details.add('Germany', '2012/08/12', '2014/09/12')


    print(details.current_country('2012/08/15'))
    print(details.locations)


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
#         """Cheching all error checking"""
#
#         dateString = input('Now check current_country by entering a date between the trip:')
#         currentCountry = object_input.current_country(dateString)
#
#         loop_check = input('check again? Y or N').upper()
#         if loop_check == 'Y':
#             loop_check = True
#         else:
#             loop_check = False
