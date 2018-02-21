import re

def word_count(phrase):
    phrase = phrase.lower()
    phrase = re.sub(r'[^\w\s\']',' ',phrase)
    phrase = re.sub(r'[_\n\t]',' ',phrase)
    phrase_arr = phrase.split(' ')
    phrase_dic = {}
    for word in phrase_arr:
        num_quote = word.count('\'')
        if num_quote is not 0 and num_quote % 2 is 0:
            word = re.sub(r'[\']','',word)
        if word is '':
            pass
        elif word not in phrase_dic:
            phrase_dic[word] = 1
        else:
            phrase_dic[word] += 1
    return phrase_dic
