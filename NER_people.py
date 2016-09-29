import cPickle, numpy as np, pandas as pd , re
from polyglot.text import Text

tagged_search = pd.read_csv('processed_search_term_data/tagged_search_terms.csv')

tagged_search_list = list(set(tagged_search['processed_search_term']))

def removePunctuation(text):

    for c in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~\\':
        text = text.replace(c,"").strip().lower()
    return text

string_word = removePunctuation(str(tagged_search_list))


def people(string):
    '''

    ****This function will work after much better if you have cleaned and identified relevant search terms first.
    Removing addresses first is key since names of streets are name of people and we dont want that.****
    
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

string = people(string_word) 

cPickle.dump(string,open('NER_people_list.p','wb'))
# creates a list of saved file
# to load:

# common_words = set(cPickle.load(open('NER_people_list.p', 'rb')))

#link:

# http://polyglot.readthedocs.io/en/latest/NamedEntityRecognition.html