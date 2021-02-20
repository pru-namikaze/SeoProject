

import json as json
import os

class QueryItemNotFoundError(Exception):
    pass;

def init_for_search(query):
    if query is "":
        print("enter a sentence:", end = '')
        query = str(input())
    query = query.strip().split()

    data_dictionary_path = os.path.join(os.path.dirname(__file__),"datadictionary/data_dictionary.json")
    result_data_dictionary_path = os.path.join(os.path.dirname(__file__),"datadictionary/result_data_dictionary.json")

    query_item_property = dict()

    for query_item in query:
        finding_Keywords_in_nested_dictionary(query_item, data_dictionary_path,query_item_property)
    write_file = open(result_data_dictionary_path, "w", encoding = "utf-8")
    json.dump(query_item_property, write_file, ensure_ascii = False)
    write_file.close()
    return query_item_property

def finding_Keywords_in_nested_dictionary(query_item, data_dictionary_path, query_item_property):
    data_dict = dict()

    data_file = open(data_dictionary_path,"r")
    data_dict.update(json.load(data_file))
    data_file.close()
    
    try:
        path = find_query_item(data_dict, query_item)
    except QueryItemNotFoundError:
        return False

    query_location_lookup = data_dict
    for key in path:
        query_location_lookup = query_location_lookup[key]
    if type(query_location_lookup) is dict:
        for key in list(query_location_lookup.keys()):
            if key.upper().lower() == query_item.upper().lower():
                query_location_lookup = query_location_lookup[key]
                path.append(key)
    
    query_item_property[query_item]={"path": path}
    #query_item_property[query_item]={"path": path, "having_or_with": query_location_lookup}


def find_query_item(data_dict, query_item):
    path_value_tuple = list()
    path_value_tuple.append((list(), data_dict))
    while path_value_tuple:
        path, query_iterating_item = path_value_tuple.pop()        
        if query_iterating_item == query_item:
            return path
        elif type(query_iterating_item) is list:
            if query_item.lower() in (query_iterating_item_name.lower() for query_iterating_item_name in query_iterating_item):
                return path
        elif type(query_iterating_item) is dict:
            if query_item.lower() in (query_iterating_item_key_name.lower() for query_iterating_item_key_name in list(query_iterating_item.keys())):
                return path 
        
        try:
            items = query_iterating_item.items()
        except AttributeError:
            continue

        for k, v in items:
            path_value_tuple.append((path + [k], v))
    raise QueryItemNotFoundError


if __name__ == '__main__':
    query = ""
    init_for_search(query)
