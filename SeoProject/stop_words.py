
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

def intit_for_stop_words():
    print('Enter Stop Word removed query:', end = '')
    query = str(input())
    query = stop_words(query)
    return query

def write_in_txt(quert_file_path, filtered_query):
    with open(quert_file_path,'w') as f:
        for i in filtered_query:
            f.write(i + ' ')
    f.close()


#query as String
def stop_words(query):

    query = query.lower()
    stop_words = set(stopwords.words('english'))
    stop_words.remove('out')
    stop_words.update('.', ',', '"', "'", '-', '&')
    
    word_tokens = word_tokenize(query)
 
    filtered_query = []
 
    for w in word_tokens:
        if w not in stop_words:
            filtered_query.append(w)

    write_in_txt(os.path.join(os.path.dirname(__file__),"NLP_Module/query.txt"), filtered_query)
    return filtered_query


if __name__ == '__main__':
    intit_for_stop_words()
