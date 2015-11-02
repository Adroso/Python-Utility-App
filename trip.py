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
        return self.currency_symbol + str(round(value, 2))

    def __str__(self):
        return str(self.name + ' ' + self.currency_code + ' ' + self.currency_symbol)


class Details:
    """Records sequence of countries visited during a trip"""

    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):

        """Error Checking Section for add()"""
        if not (isinstance(country_name, str) or isinstance(start_date, str) or isinstance(end_date, str)):
            raise TypeError('Error, Input data is meant to be text')

        if not datetime.datetime.strptime(start_date, '%Y/%m/%d') or not datetime.datetime.strptime(end_date,
                                                                                                    '%Y/%m/%d'):
                raise ValueError  # ValueError used over Error to avoid Exit statement

        for location in self.locations:
            if start_date in location[1]:
                raise Error('There is a duplicate start date in the list')

        if start_date > end_date:
            raise Error('Start Date is after End Date')

        self.locations.append((country_name, start_date, end_date))
        return self.locations

    def current_country(self, date_string):
        if not datetime.datetime.strptime(date_string, '%Y/%m/%d'):
            raise ValueError  # ValueError used over Error to avoid Exit statement

        for location in self.locations:
            # Convert Strings inputs to dates for comparison
            date_input = datetime.datetime.strptime(date_string, '%Y/%m/%d').date()
            initial_date = datetime.datetime.strptime(location[1], '%Y/%m/%d').date()
            final_date = datetime.datetime.strptime(location[2], '%Y/%m/%d').date()

            if initial_date <= date_input <= final_date:
                return location[0]
        raise Error('There is no country for this date')

    def is_empty(self):
        if len(self.locations) == 0:
            return True  # Empty locations
        else:
            return False  # values in locations


if __name__ == "__main__":

    """ Module Testing"""
    print('READY...')
    print('TEST')

    # Country() Testing
    test1 = Country('Germany', 'EUR', '€')
    print('Testing Country()')
    print('Formatting Currency Test Expected,€100 $(amount) :', test1.format_currency(100))
    print('String Formatting Change Expected, Name Currency_Code Currency_Symbol:', str(test1))
    print('')
    print('Testing Details()')
    details = Details()
    print('Date conforms to correct format Details added', details.add('Australia', '2014/09/12', '2014/09/14'))

    test_int = 3
    print('Inputs Text expected error, needs to be str not int:')
    try:
        details.add('France', test_int, "2014/09/14")
    except TypeError as err:
        print(err)

    print('Invalid input, wrong date format (extra digits) vv')
    try:
        details.add('Japan', '201378/11/13', '2014/12/12')
    except ValueError as err:
        print(err)
    print('Invalid input, wrong date format (year last) vv')
    try:
        details.add('Japan', '2013/11/13', '20/12/1209')
    except ValueError as err:
        print(err)

    print('')
    # Testing start date check
    print('Invalid Input start date is after end date:')
    try:
        details.add('Japan', '2015/11/01', '2013/11/01')
    except Error as err:
        print(err)
    print('Valid Input Saudi Arabia and details added:')
    try:
        test2 = details.add('Saudi Arabia', '2013/11/01', '2013/11/05')
        print(test2)
    except Error as err:
        print(err)
    print('')

    # Testing a previous date
    print('Invalid Input date 2013/11/01 was used before:')
    try:
        test3 = details.add('USA', '2013/11/01', '2013/11/05')

    except Error as err:
        print(err)

    print('Valid Input, USA is added:')
    try:
        test3 = details.add('United States of America', '2014/11/01', '2014/11/05')
        print(test3)
    except Error as err:
        print(err)
    print('')

    # Testing current_country

    print('Input date is already in locations, returns country name:')
    try:
        test4 = details.current_country('2014/11/02')
        print(test4)
    except Error as err:
        print(err)

    print('Invalid Input, no record of a current country:')
    try:
        test4 = details.current_country('2016/11/02')
        print(test4)
    except Error as err:
        print(err)
    print('')

    # Testing is_empty()
    print('Testing is_empty')
    print('locations has data - Expected False:', details.is_empty())


    details.locations = []
    print('Testing is_empty')
    print('locations is empty - Expected True:', details.is_empty())



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
