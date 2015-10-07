__author__ = 'Adroso'

import web_utility

def convert(amount, home_currency_code, location_currency_code): # This function takes in input data from a home currency and converts it to another by returning the converted amount.

    amount_as_string = str(amount) #Convert to string here because you can not join str and int implicitly

    input_url = "https://www.google.com/finance/converter?a=" + amount_as_string + "&from=" + home_currency_code + "&to=" + location_currency_code #building the search URL

    print(input_url) #checking

    web_utility.load_page(input_url)




    return

def get_details(country_name): # This function interprets data from a file

    currency_details = open("currency_details.txt", 'r') #load the currency details file as read
    import re

    for line in currency_details: #loops to each line
        if country_name in line: #Searches for the input within the string (DOES NOT SEARCH FOR EXACT)
            return print(line)
    currency_details.close()
    return ();


convert(86.5, 'JPY', 'AUD')
country_name = input("Country")
get_details(country_name)


