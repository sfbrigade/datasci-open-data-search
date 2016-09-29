import cPickle, numpy as np, pandas as pd , re
from collections import Counter
from polyglot.text import Text

tagged_search = pd.read_csv('processed_search_term_data/tagged_search_terms.csv')

tagged_search_list = list(tagged_search['processed_search_term'])

def removePunctuation(text):

    for c in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~\\':
        text = text.replace(c,"").strip().lower()
    return text

string_word = removePunctuation(str(tagged_search_list))


def people(string):
    '''
    This function will work after much better if you have cleaned 
    and identified relevant search terms.
    
    Input: A string of relevant search terms
    Output: pulls out names of people identified from the Named Entity Recognition 
    software polyglot
    '''
    NER = Text(string)
    NER = NER.entities
    ent = [removePunctuation(re.sub('I-PER','',str(entity))) for entity in NER if entity.tag == "I-PER"]
    ent =[' '.join(set([w[1:] for w in word.split(' ')])) for word in ent]
    return list((ent))

string = people(string_word) 

S = Counter(string).most_common()

name = []
count = []

for name_count in (S):
    name.append(name_count[0])
    count.append(name_count[1])

table = pd.DataFrame(columns=['Name','Count'])

table['Name'] = name
table['Count'] = count

table.to_csv('people_count.csv')

#cPickle.dump(string,open('NER_people_list.p','wb'))
# creates a list of saved file
# to load:

# common_words = set(cPickle.load(open('NER_people_list.p', 'rb')))

#link:

# http://polyglot.readthedocs.io/en/latest/NamedEntityRecognition.html