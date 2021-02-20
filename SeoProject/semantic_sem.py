import nltk
from nltk.corpus import wordnet
#import lemma

def calculate(queryv,queryn,queryr,verb,noun,adverb):
    tot = 0; count = 1
    lqv = len(queryv)
    lqn = len(queryn)
    lqr = len(queryr)
    lv = len(verb)
    ln = len(noun)
    lr = len(adverb)
    f = open('semantic_data.txt','a+')
    #compare verbs of query and meta description
    for i in range(lqv):
        for j in range(lv):
            try:
                w1 = wordnet.synset(queryv[i])
                w2 = wordnet.synset(verb[j])
                #print(w1)
                t1 =w1.wup_similarity(w2)
                #print(t1)
                f.write("\n"+queryv[i]+"\t\t\t"+verb[j]+"\t\t\t\t"+str(t1))
                tot += t1
                count += 1
            except:
                pass
    #print(tot)
    f.write("\n"+str(tot)+"\n")
    #compare nouns of query and meta description
    for i in range(lqn):
        for j in range(ln):
            try:
                w1 = wordnet.synset(queryn[i])
                w2 = wordnet.synset(noun[j])
                #print(w1)
                t2 = w1.wup_similarity(w2)
                #print(t2)
                f.write("\n" + queryn[i] + "\t" + noun[j] + "\t\t" + str(t2))
                tot += t2
                count += 1
                #print(sum)
            except:
                pass
    #print(tot)
    f.write("\n"+str(tot) + "\n")
    #compare adverbs of query and meta description
    for i in range(lqr):
        for j in range(lr):
            try:
                w1 = wordnet.synset(queryr[i])
                w2 = wordnet.synset(adverb[j])
                #print(w1)
                t3 = w1.wup_similarity(w2)
                #print(t3)
                f.write("\n" + queryr[i] + "\t" + adverb[j] + "\t\t" + str(t3))
                tot += t3
                count += 1
            except:
                pass
    #print(tot/count)
    f.write("\n"+str(tot) + "\n" + "Rel_value=" + str(tot/count))
    f.close()
    return tot/count



