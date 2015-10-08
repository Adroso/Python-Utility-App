__author__ = 'Adroso'

import web_utility

def convert(amount, home_currency_code, location_currency_code):  # This function takes in input data from a home currency and converts it to another by returning the converted amount.
    import re

    amount_as_string = str(amount)   #Convert to string here because you can not join str and int implicitly
    try:
        input_url = "https://www.google.com/finance/converter?a=" + amount_as_string + "&from=" + home_currency_code + "&to=" + location_currency_code #building the search URL



        output_code = web_utility.load_page(input_url)

        span_start = output_code.find('class=bld>')  #The value is in the only span class
        span_end = output_code.find('</span>')

        span_container = output_code[span_start:span_end]  #gives the span container as a string
        currency_with_code = span_container.split('class=bld>')  #Takes the leading span tag out
        separated_code_currency = currency_with_code[1]  #separates value and  country code
        converted_currency = separated_code_currency.split(' ') #iscolates value

        return converted_currency[0]
    except:
        return -1


def get_details(country_name):  # This function interprets data from a file]

    currency_details = open("currency_details.txt", 'r')  #load the currency details file as read

    for line in currency_details:  #loops to each line
        current_line = line.split(",")
        if country_name in line:  #Searches for the input within the string (DOES NOT SEARCH FOR EXACT)
            if country_name == current_line[0]:
                return current_line
            else:
                return ()
    currency_details.close()
    return ()


print(convert(1, 'AUD', 'JPY'))
country_name = input("Input Test Country:")
print(get_details(country_name))
