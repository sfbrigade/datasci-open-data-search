import numpy as np, pandas as pd , re
from polyglot.text import Text

street_names = pd.read_csv('street_names_clean.csv')

street_name_list = list(street_names['Names'].values)

query = pd.read_csv("./data/all_queries.csv")

keywords = list(query['ga.searchKeyword'].values)

def removePunctuation(text):

    for c in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~':
        text = text.replace(c,"").strip().lower()
    return text

string_word = removePunctuation(str(keywords))


def people(string):
    '''

    This function will work after much better if you have cleaned and identified relevant search terms.
    
    Input: A string of relevant search terms
    Output: pulls out names of people identified from the Named Entity Recognition software polyglot

    The function actives the Text class and then uses the entities function to identify person organization and 
    location.  It isolates only for persons, gets rid of I-PER statement and the 'u' statement in the beginning
    of unicode strings and joins the string back together, it does a set of each list and then the overall list
    to rid of duplicate findngs.  

    '''
    NER = Text(string)
    NER = NER.entities
    ent = [removePunctuation(re.sub('I-PER','',str(entity))) for entity in NER if entity.tag == "I-PER"]
    ent =[' '.join(set([w[1:] for w in word.split(' ')])) for word in ent]
    return list(set(ent))

people(string_word)

#link:

# http://polyglot.readthedocs.io/en/latest/NamedEntityRecognition.html