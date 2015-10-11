__author__ = 'Adroso'

import web_utility


def convert(amount, home_currency_code, location_currency_code):
    """ This function takes in an amount, generates a url to use Googles currency conversion service and extracts
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

        return converted_currency[0]
    except:
        return -1


def get_details(country_name):  # This function interprets data from a file]

    currency_details = open("currency_details.txt", 'r', encoding='utf-8')  # load the currency details file as read

    for line in currency_details:
        current_line = line.split(",")  # Splits data by commas to be exact matched in the following lines
        if country_name in line:  # Searches for match in line
            if country_name == current_line[0]:  # Checks if the country name exactly matches the one in line.
                return current_line
            else:
                return ()
    currency_details.close()
    return ()


""" Module Testing"""

if __name__ == "__main__":

    print()











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
