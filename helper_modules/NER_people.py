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

def LOC(string):
    '''
    This function will work after much better if you have cleaned 
    and identified relevant search terms.
    
    Input: A string of relevant search terms
    Output: pulls out names of people identified from the Named Entity Recognition 
    software polyglot
    '''
    NER = Text(string)
    NER = NER.entities
    ent = [removePunctuation(re.sub('I-LOC','',str(entity))) for entity in NER if entity.tag == "I-LOC"]
    ent =[' '.join(set([w[1:] for w in word.split(' ')])) for word in ent]
    return list((ent))

Location = LOC(string_word) 

Location_counter = Counter(Location).most_common()
loc = []
cnt = []

for loc_count in (Location_counter):
    loc.append(loc_count[0])
    cnt.append(loc_count[1])

table1 = pd.DataFrame(columns=['Name','Name_Count'])
table2 = pd.DataFrame(columns=['Location','Location_Count'])
table1['Name'] = name
table1['Count'] = count
table2['Location'] = loc
table2['Location_Count'] = cnt

table1.to_csv('people_count.csv')
table2.to_csv('location_count.csv')

#link:

# http://polyglot.readthedocs.io/en/latest/NamedEntityRecognition.html