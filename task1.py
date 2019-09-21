import json
import requests
from bs4 import BeautifulSoup

def get_conf(file_name):
    fo = open(file_name,'r')
    x=fo.readlines()
    dict1= json.loads(x[0])
    return dict1

def get_search_text(search_engine_link,key):
    search_url = str(search_engine_link) + str(key)
    res = requests.get(search_url)
    if res.status_code == 200:
        return res.text
    else:
        return "error"

conf_dict = get_conf("conf.json")
print(conf_dict)

import csv

search_count_dict= {}
for key in conf_dict.keys():
    print(conf_dict[key])
    key_str = input("enter search string:")
    text_content = get_search_text(conf_dict[key],key_str)
    print(len(text_content))
    soup = BeautifulSoup(text_content,features="html.parser")
    count = 0
    for link in soup.find_all('a'):
        count +=1
	#print(link.get('href'))
    search_count_dict[key] = count
print(search_count_dict)
    
f1 = open("search_results-count.txt",'w')
head_str = ''
for k1 in search_count_dict.keys():
    head_str = str(head_str) + str(k1) +str(',')
f1.write(head_str)
f1.write('\n')
value_str = ''
for k1 in search_count_dict.values():
    value_str = str(value_str) + str(k1)+str(',')

f1.write(value_str)
f1.write('\n')
f1.close()
    
