from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stop(query):
    query = query.lower()

    stop_words = set(stopwords.words('english'))
    stop_words.remove('out')
    stop_words.update('.', ',', '"', "'", '-', '&',':','%')
    #print(stop_words)
    word_tokens = word_tokenize(query)
    query = set(query)
    query = list(query)
    #print(word_tokens)
    filtered_query = []

    for w in word_tokens:
        if w not in stop_words:
            if w.startswith(r'\n'):
                w = w[2:]
            elif w.startswith(r'"'):
                w = w[1:]
            filtered_query.append(w)

    try:
        filtered_query.remove('...')
        filtered_query.remove(r'``')
        filtered_query.remove('"')
        filtered_query.remove("'s")
    except:
        pass

    #print(filtered_query)
    return filtered_query



from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize
from nltk import pos_tag


def lemm(text):
	verb_pos_tags = ['VB','VBD','VBG', 'VBN', 'VBP', 'VBZ']
	noun_pos_tags = ['NN','NNS','NNP','NNPS']
	adverb_pos_tags = ['RB','RBR','RBS']
	mod_pos = list()
	pos = pos_tag(text)
	#print(pos)
	l = len(pos)
	for i in range(l):
		pos[i] = list(pos[i])
	#print(pos)
	l = len(pos)
	#print(l)
	lemmatizer = WordNetLemmatizer()
	for i in range(l):
		if pos[i][1] in verb_pos_tags:
			#pos[i][1] = 'v'
			mod_pos.append([pos[i][0],'v'])
		elif pos[i][0].endswith('ing'):
			#pos[i][1] = 'v'
			mod_pos.append([pos[i][0], 'v'])
		elif pos[i][1] in noun_pos_tags:
			#pos[i][1] = 'n'
			mod_pos.append([pos[i][0], 'n'])
		elif pos[i][1] in adverb_pos_tags:
			#pos[i][1] = 'n'
			mod_pos.append([pos[i][0], 'r'])
		else:
			pass
	#print(mod_pos)
	ll = len(mod_pos)
	mod_pos_verb = list()
	mod_pos_noun = list()
	mod_pos_adverb = list()
	for i in range(ll):
		mod_pos[i][0] = lemmatizer.lemmatize(mod_pos[i][0],mod_pos[i][1])
		if mod_pos[i][1] == 'v':
			mod_pos_verb.append(mod_pos[i][0]+'.v.01')
		elif mod_pos[i][1] == 'n':
			mod_pos_noun.append(mod_pos[i][0]+'.n.01')
		elif mod_pos[i][1] == 'r':
			mod_pos_adverb.append(mod_pos[i][0]+'.r.01')

	'''print(mod_pos)
	print(mod_pos_verb)
	print(mod_pos_noun)'''
	return mod_pos_verb,mod_pos_noun,mod_pos_adverb
	#print(pos)
