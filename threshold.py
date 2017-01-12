from fuzzywuzzy import fuzz

def removePunctuation(text):
    '''
    input: string of words
    output: punctuation and special characters removed
    '''
    for c in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~\\':
        text = text.replace(c,"").strip().lower()
    return text
        

def threshold(word):
    word = removePunctuation(word)
    fuzzy = []
    word_list = open('word_list.txt').read().replace("\n",' ').split(' ')
    for w in word_list:
        fuzzy.append(fuzz.ratio(word, w))
    return max(fuzzy)