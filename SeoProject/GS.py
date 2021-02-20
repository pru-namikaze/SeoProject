'''
    Scrapping first 40 results of google search
'''

import requests
from bs4 import BeautifulSoup
import sys
import json

from lxml import html

class GoogleScrapping:

    url = "http://www.google.com/search?num=50&q=news"
    search_result_header = []
    search_result_link = []
    search_result_details = []
    
    def __init__(self, mod_query):

        '''
	    with open('query_upgrade.txt', 'r') as f:
            query = f.read()

        '''
        if mod_query == "":
            while True:
                query = input('Enter the topic to be searched...\n')
                if query is None:
                    print('Query cannot be empty')
                else:
                    break
        else:
            query = mod_query
        query = self.__format_query(query)
        self.url += query
        self.__scrap_query_result()

    def __format_query(self, query):
            query = query.strip().split()
            mod_query = str()
            for en in query:
                mod_query = mod_query + "+" + en
            return mod_query

    def __scrap_query_result(self):

        source_code = requests.get(self.url)
        soup = BeautifulSoup(source_code.text, 'lxml')

        # Soup headers        
        for header_tag in soup.find_all('h3', attrs={'class':'LC20lb DKV0Md'}):
            if header_tag.find('a') and 'Images for ' not in header_tag.text and 'News for ' not in header_tag.text and 'Videos for ' not in header_tag.text:
                self.search_result_header.append(header_tag.text)

        # Soup links
        for cite_tag in soup.find_all('cite'):
                
            search_result = cite_tag.text.replace(' ', '')
            if '.' in search_result:
                if not str(search_result).startswith('http'):
                    search_result = 'http://' + search_result
                self.search_result_link.append(search_result)

        # Soup details
        for span_tag in soup.find_all('span', attrs={'class':'st'}):
            self.search_result_details.append(span_tag.text)

def prep_for_inbound(dic, lemma_query):
    
    daa = dict()
    more_content = str()
    query = str()

    for en in dic.keys():
        path = dic[en]["path"]
        temp_str = " ".join(path)
        more_content = more_content.strip() + " " + temp_str.strip() + " "
    query = lemma_query + more_content
    daa = init_for_crawler(query)
    return daa
    
def init_for_crawler(mod_query):

    googleScrapping = GoogleScrapping(mod_query)

    l = []
    l.append(len(googleScrapping.search_result_link))
    l.append(len(googleScrapping.search_result_details))
    l.append(len(googleScrapping.search_result_header))
    l.sort()
    dic = {}
    for i in range(l[0]):
        dic[i] = {"header": googleScrapping.search_result_header[i]
        ,   "detail": googleScrapping.search_result_details[i]
        ,   "link": googleScrapping.search_result_link[i]
            }

    # Storing the info into json style in .txt file
    write_file = open("resultDic" + ".json", "w", encoding="utf-8")
    json.dump(dic, write_file, ensure_ascii=False, indent=4)
    write_file.close()
    return dic

 
if __name__ == "__main__":
    mod_query = ""
    init_for_crawler(mod_query)