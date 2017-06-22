"""
This function is help identify and label keywords and phrases that are used in the
SF open data portal.  This is aimed to segment the bad search terms such as addresses, the web links,
and the actual relevant keyword search used.  

"""
import pandas as pd
import re


# Load San Francisco Street Data
street_names = pd.read_csv('street_names_clean.csv')
street_name_list = list(street_names['Names'].values)



def removePunctuation(text):
    '''
    Removes Punctuation from Input Text
    :param text: Text Input
    :return: Text free of punctuation
    '''

    for c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(c,"").strip().lower()
    return text


def searchAddress(text):
    '''
    Identifies if text is an address in San Francisco
    :param text: Text Input
    :return:
    '''
    result = [re.findall('\d+\s' + street + '|' + street + '\s\w+', text) for street in street_name_list
              if re.findall('\d+\s' + street + '|' + street + '\s\w+', text) ]
    return result


def search_term_type(text):
    
    """
    input: keyword search term
    output: labels the keyword as good, address, year, link.
    
    """
    #street_type = '\s(aly|ave*|blvd|boulevard|cir*|court|ct|dr*|exp*|hl|hwy|highway|ln|lane|park|path|pl*|ramp|rd|road|row|st*|step*|stps|walk|way)'
    
    processed_text = removePunctuation(text)

    # address = [re.findall('\d+\s'+street+'|'+street+'\s\w+',text) for street in street_name_list
    #            if re.findall('\d+\s'+street+'|'+street+'\s\w+', text)!= []]

    # Regex patterns
    dates_regex = re.compile("[0-9]*[0-9]/[0-9]*[0-9]/[0-9]*[0-9]")
    links_regex = re.compile("http[s]*|www.*")
    numbers_regex = re.compile("^[0-9][0-9]*[0-9]$")
    valid_numbers = ['311', '911']
    address_regex = re.compile('^[0-9]*[0-9] [a-z]*[a-z]')

    # Series of checks for categorizing search terms
    if bool(re.search(links_regex,text)):
        term_category = "Link"
    elif bool(re.search(dates_regex,text)):
        term_category = "Date"

    elif bool(re.search(numbers_regex, text)):
        if text in valid_numbers:
            term_category = "Search Term"
        else:
            term_category = "Number"

    # Checks for SPELLING ERRORS


    # if not one of the previous check if address
    else:
        if bool(re.search(address_regex, text)):
            address = searchAddress(processed_text)

            if bool(address):
                term_category = "Address"
            else:
                term_category = "Search Term"
        else:
            term_category = "Search Term"

    #find_links = re.findall(links_regex, text)

    return term_category

# http://stackoverflow.com/questions/6718633/python-regular-expression-again-match-url
# http://regexlib.com/REDetails.aspx?regexp_id=430

# For testing
print search_term_type("1190 mission street")

print search_term_type("09/11/2105")
print search_term_type("www.google.com")

print search_term_type("911")
print search_term_type("555 doctor")