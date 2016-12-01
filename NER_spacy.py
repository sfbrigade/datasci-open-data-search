import spacy
from collections import defaultdict
nlp = spacy.load('en')


def removePunctuation(text):

    for c in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~':
        text = text.replace(c,"").strip().lower()
    return text


def NER(string):
    '''
    Input: String
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