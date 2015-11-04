__author__ = 'Adroso'

import web_utility


def convert(amount, home_currency_code, location_currency_code):
    """ This function takes in an amount, generates a url to use Goggles currency conversion service and extracts
    the converted value """

    amount_as_string = str(amount)  # Convert to string here because you can not join str and int implicitly
    try:
        input_url = "https://www.google.com/finance/converter?a=" + amount_as_string + "&from=" + home_currency_code + \
                    "&to=" + location_currency_code  # building the search URL

        output_code = web_utility.load_page(input_url)

        span_start = output_code.find('class=bld>')  # The value is in the only span class
        span_end = output_code.find('</span>')
        span_container = output_code[span_start:span_end]  # gives the span container as a string

        currency_with_code = span_container.split('class=bld>')  # Takes the leading span tag out
        separated_code_currency = currency_with_code[1]  # separates value and  country code
        converted_currency = separated_code_currency.split(' ')  # isolates value

        return float(converted_currency[0])
    except IndexError:  # Raised when a sequence subscript is out of range.
        return -1


def get_details(country_name):
    """This function interprets data from a file"""

    currency_details = open("currency_details.txt", 'r', encoding='utf-8')

    for line in currency_details:
        current_line = line.split(",")  # Splits data by commas to be exact matched in the following lines
        if country_name in line:
            if country_name == current_line[0]:  # Checks if the country name exactly matches the one in line.
                line_details = current_line.strip('\n')
                return line_details
            else:
                return ()
    currency_details.close()
    return ()

def get_all_details():
    """This function returns a dictionary of currency details"""

    all_country_details = {}

    details_file = open("currency_details.txt", 'r', encoding='utf-8')
    for line in details_file:
        split_details = line.split(",")
        all_country_details[split_details[0]] = (split_details[0], split_details[1], split_details[2])
        details_file.close()
    return all_country_details




""" Module Testing"""

if __name__ == "__main__":
    print('TESTING')
    print('')
    print('Test of convert()')
    print("invalid conversion expect: -1", "1", "AUD", "->", "AUD", "=", convert(1, "AUD", "AUD"))
    print("invalid conversion expect: -1", "1", "JPY", "->", "ABC", "=", convert(1, "JPY", "ABC"))
    print("invalid conversion expect: -1", "1", "ABC", "->", "USD", "=", convert(1, "ABC", "USD"))
    print("valid conversion", "10.95", "AUD", "->", "JPY", "=", convert(10.95, "AUD", "JPY"))
    print("valid conversion reverse", "965.71", "JPY", "->", "AUD", "=", convert(965.71, "JPY", "AUD"))
    print("valid conversion", "10.95", "AUD", "->", "BGN", "=", convert(10.95, "AUD", "BGN"))
    print("valid conversion reverse", "13.82", "BGN", "->", "AUD", "=", convert(13.82, "BGN", "AUD"))
    print("valid conversion", "200.15", "BGN", "->", "JPY", "=", convert(200.15, "BGN", "JPY"))
    print("valid conversion reverse", "13390.51", "JPY", "->", "BGN", "=", convert(13390.51, "JPY", "BGN"))
    print("valid conversion", "100", "JPY", "->", "USD", "=", convert(100, "JPY", "USD"))
    print("valid conversion reverse", "0.83", "USD", "->", "JPY", "=", convert(0.83, "USD", "JPY"))
    print("valid conversion", "19.99", "USD", "->", "BGN", "=", convert(19.99, "USD", "BGN"))
    print("valid conversion reverse", "34.39", "BGN", "->", "USD", "=", convert(34.39, "BGN", "USD"))
    print("valid conversion", "19.99", "USD", "->", "AUD", "=", convert(19.99, "USD", "AUD"))
    print("valid conversion reverse", "27.26", "AUD", "->", "USD", "=", convert(27.26, "AUD", "USD"))
    print('')
    print('Testing get_details()')

    print("invalid details expect ():", get_details("Unknown"))
    print("invalid details expect ():", get_details("Japanese"))
    print("invalid details expect ():", get_details(""))
    print("valid details expect details of AUS:", get_details("Australia"))
    print("valid details expect details of JPN:", get_details("Japan"))
    print("valid details expect details of HK:", get_details("Hong Kong"))

    # New get_all_details testing:
    print(get_all_details())
    testing = get_all_details()
    print("keys", testing.keys())
    print(testing["Australia"])


    # Manual Testing
    # converted_save = 0
    #
    # loop_check = True
    # while loop_check:
    #
    #     amount = input('Amount to change:') # Assume value will be a number
    #     home = str(input('Home Currency Code:'))
    #     away = str(input('Away Currency Code:'))
    #
    #     converted = convert(amount, home, away)
    #
    #     if converted == -1:
    #         check = 'invalid conversion'
    #     elif converted_save == amount:
    #         check = 'valid conversion reverse'
    #     else:
    #         check = 'valid conversion'
    #
    #     converted_save = converted
    #
    #     print(check, ' ', amount, ' ', home, '->', away, ' ', converted)
    #
    #     loop_check = input('check again or move on to next check? Y or N').upper()
    #     if loop_check == 'Y':
    #         loop_check = True
    #     else:
    #         loop_check = False
    #
    # loop_check = True
    # while loop_check:
    #     country_name = input("Input Test Country:").title()
    #     details = get_details(country_name)
    #
    #     if not details:
    #         check = 'invalid details'
    #     else:
    #         check = 'valid details'
    #
    #     print(check, ' ', country_name, ' ', details)
    #
    #     loop_check = input('check again or finnish? Y or N').upper()
    #     if loop_check == 'Y':
    #         loop_check = True
    #     else:
    #         loop_check = False
    #         print('Thank You :)')
