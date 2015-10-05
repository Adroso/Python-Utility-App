__author__ = 'Adroso'

import web_utility

def convert(): # This function takes in input data from a home currency and converts it to another.

    web_utility.load_page('https://www.google.com/finance/converter?a=1&from=AUD&to=JPY')
    return

def get_details(country_name): # This function interprets data from a file

    currency_details = open("currency_details.txt", 'r') #load the currency details file as read
    import re
    for line in currency_details: #loops to each line
        if country_name in line: #Searches for the input within the string (DOES NOT SEARCH FOR EXACT)
            return print(line)
    currency_details.close()
    return ();


convert()
country_name = input("Country")
get_details(country_name)

