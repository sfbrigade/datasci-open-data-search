__author__ = 'Baolin Liu'

import spacy
from collections import defaultdict
import os

try:
    nlp = spacy.load('en')
except RuntimeError:
    bashCommand = "python -m spacy.en.download"
    os.system(bashCommand)
    

'''

Based on my experience , only "PERSON" , "ORG" , "FAC" only gave anything useful

PERSON - People, including fictional.

ORG	- Companies, agencies, institutions, etc.

FACILITY - Buildings, airports, highways, bridges, etc.


'''

def removePunctuation(text):

    # for c in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~':
    #     text = text.replace(c,"").strip().lower()
    # return text

    p = '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
    text = filter(lambda x : x not in p, s)
    text = map(lambda x : x.strip(), text.split())

    return ' '.join(text)


def NER(string):
    '''
    Input: String contain names, location, companies , etc.
    Output: Dictionary of Named Entities
    '''
    string = removePunctuation(string)
    s = string.title()
    doc = nlp(unicode(s))
    d = defaultdict(list)
    
    for ent in doc.ents:
        d[ent.label_].append(ent.text)
    return d

    '''
    https://spacy.io/docs/usage/entity-recognition

    '''

'''

Example:

S = NER(string_word)

print S['PERSON']

print S['ORG']

print S['FAC']

'''

