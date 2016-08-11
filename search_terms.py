# removing punctuation

def removePunctuation(text):

    for c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(c,"").strip().lower()
    return text


def search_term_type(text):
    
    """
    input: keyword search term
    output: labels the keyword as good, address, link.
    
    """
    
    text = removePunctuation(text)
    address = [re.findall('\d\s'+street,text) for street in street_name_list 
               if re.findall('\d\s'+ street, text)!= []]
    
    links_regex = "http[s]*|www.*"

    find_links = re.findall(links_regex, text)
    
    if len(address)> 0:
        term = "Address"
    
    elif len(find_links)> 0:
        term =  "Link"
    else:
        term = "Search Term"
    return term

# http://stackoverflow.com/questions/6718633/python-regular-expression-again-match-url
# http://regexlib.com/REDetails.aspx?regexp_id=430