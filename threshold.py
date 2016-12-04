from fuzzywuzzy import fuzz

def threshold(word):
    word = removePunctuation(word)
    fuzzy = []
    word_list = open('word_list.txt').read().replace("\n",' ').split(' ')
    for w in word_list:
        fuzzy.append(fuzz.ratio(word, w))
    return max(fuzzy)