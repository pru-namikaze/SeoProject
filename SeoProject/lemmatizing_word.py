
import os
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def unit_test_lemmatizing_word():
    print('Enter Stop Word removed query:', end = '')
    stop_rem_query = str(input())
    stop_rem_query = stop_rem_query.strip()
    pos = list()
    pos = lemmatizing_word(stop_rem_query)
    print(pos)

def lemmatizing_word_with_txt():
	with open(os.path.join(os.path.dirname(__file__),"NLP_Module/query.txt"),'r') as f:
	    text = f.read()
	f.close()
	pos = list()
	pos = lemmatizing_word(text)
	print(pos)

def lemmatizing_word(text):
    if type(text) is list:
    	pos = pos_tag(text)
    elif type(text) is str():
        pos = pos_tag(word_tokenize(text))
    lemmatizer = WordNetLemmatizer()
    verb_pos_tags = ['VB','VBD','VBG', 'VBN', 'VBP', 'VBZ']
    f = open(os.path.join(os.path.dirname(__file__),"NLP_Module/query_upgrade.txt"),'w')

    for i in range(0, len(pos)):
        pos[i] = list(pos[i])
        if pos[i][1] in verb_pos_tags:
            pos[i][1] = 'v'
        elif pos[i][0].endswith('ing'):
            pos[i][1] = 'v'
        else:
            pos[i][1] = 'n'
        pos[i][0] = lemmatizer.lemmatize(pos[i][0], pos[i][1])
        f.write(pos[i][0])
        f.write(' ')
    f.close()
    with open(os.path.join(os.path.dirname(__file__),"NLP_Module/query_upgrade.txt"),'r') as f:
        lemmatized_query = f.read()
    f.close()
    return lemmatized_query

if __name__ == '__main__':
    unit_test_lemmatizing_word()    
