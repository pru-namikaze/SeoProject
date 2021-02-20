import json
from SeoProject import nlp_process
from SeoProject import semantic_sem
from SeoProject import final_rank

def init_for_rerank(daa, mod_query):
    #semantic similarity file, erasing previous content
    open('semantic_data.txt','w').close()
    
    if not bool(daa):
        #obtain result page from json
        with open('input_result_page.json','r',encoding='utf=8') as data:
            daa = json.load(data)
            #data.close()

    if not(type(mod_query) is str):
        #obtain query from json
        with open('query.json','r') as qy:
            mod_query = json.load(qy)
            qy.close()

    return page_rerank(daa, mod_query)


def page_rerank(daa, mod_query):
    index_lst = list()
    detail_list = list()
    imported_details = [[0] * len(daa)]
    for id,j in daa.items():
        index_lst.append(id)
        for k in j:
            if k == 'detail':
                detail_list.append(j[k])
    
    newlist = [[0]*2 for i in range(len(index_lst))]
    for i in range(len(index_lst)):
        newlist[i][0] = i+1
    
    #Analysis and separating query based on POS
    query = nlp_process.stop(mod_query)
    query = list(query)
    verb_query, noun_query, adverb_query = nlp_process.lemm(query)
    
    #Analysis and separating meta description
    for i in range(len(index_lst)):
        meta_descrip = detail_list[i]
    
    #stop_word removal
        filtered_meta = nlp_process.stop(meta_descrip)
        filtered_meta = list(filtered_meta)
    
    #lemmatizing
        verb_pos, noun_pos, adverb_pos = nlp_process.lemm(filtered_meta)
    
    #calculate semantic semalarity
        relevance_val = semantic_sem.calculate(verb_query,noun_query,adverb_query,verb_pos,noun_pos,adverb_pos)
    
    #calculate importance value
        final_index  = final_rank.val(i+1, relevance_val)
    
    #appending new value to list of index
        newlist[i][1] = final_index
    
    #sorting list based on new indices
    newlist = sorted(newlist, key=lambda nwlist: nwlist[1])
    
    #reversing list as highest value denotes highest rank
    newlist.reverse()
    
    list_no =list()
    #re_index_SERP = dict()
    re_index_SERP = list()

    for en in newlist:
        list_no.append(en[0])
    for en in range(0, len(list_no)):
        re_index_SERP.append(daa[list_no[en] - 1])

    #a new file result_page.json with reindexed contents
    write_file = open("output_result_page.json", "w", encoding="utf-8")
    json.dump(re_index_SERP, write_file, ensure_ascii=False, indent=4)
    write_file.close()
    #
    write_file = open("input_result_page.json", "w", encoding="utf-8")
    json.dump(daa, write_file, ensure_ascii=False, indent=4)
    write_file.close()

    return re_index_SERP

if __name__ == '__main__':
    daa = dict()
    mod_query = dict()
    init_for_rerank(daa, mod_query)   