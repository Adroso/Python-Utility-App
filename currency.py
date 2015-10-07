__author__ = 'Adroso'

import web_utility

def convert(amount, home_currency_code, location_currency_code): # This function takes in input data from a home currency and converts it to another by returning the converted amount.
    import re

    amount_as_string = str(amount) #Convert to string here because you can not join str and int implicitly
    try:
        input_url = "https://www.google.com/finance/converter?a=" + amount_as_string + "&from=" + home_currency_code + "&to=" + location_currency_code #building the search URL

        #print(input_url) #checking

        output_code = web_utility.load_page(input_url)

        span_start = output_code.find('class=bld>') #The value is in the only span class
        span_end = output_code.find('</span>')


        span_container = output_code[span_start:span_end] #gives the span container as a string
        converted_currency = float(span_container[10:16]) #pulls the number as a float.

        #print(converted_currency) #checking
        return converted_currency
    except:
        return -1


def get_details(country_name): # This function interprets data from a file

    currency_details = open("currency_details.txt", 'r') #load the currency details file as read


    for line in currency_details: #loops to each line
        if country_name in line: #Searches for the input within the string (DOES NOT SEARCH FOR EXACT)
            return print(line)
    currency_details.close()
    return ();


print(convert(1, 'AUD', 'JPY'))
country_name = input("Country")
get_details(country_name)


