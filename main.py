import shelve



__author__ = 'Girish'

from scrapper.Snippet import Snippet
from scrapper.DataFinder import DataFinder
import json

import sys
if len(sys.argv) <2:
    print("Havent entered the name of the question")
    sys.exit(-1)
data =0
try:
    with open("data") as store:
        if store.readable():
            data = int(store.read())
        else:
            print("you dont have to permission to read or write")
            sys.exit(0)
except PermissionError:
    print("no permission to read the file")
except Exception:
    pass

try:
    def find(name,data):
        name = name.lower()
        name = name.strip()
        with shelve.open("data",writeback=True) as data_store:
            if name in data_store.keys():
                return data, data_store[name]

            disp =["\\",'|','/','-']

            datafetcher = DataFinder("http://www.spoj.com/problems/classical/sort=0,start={start}",start=data)
            html_snippet = Snippet(Snippet.SPOJ)
            ind=0
            for i in datafetcher.get_page():
                for w in html_snippet.get_data_dicts(i):
                    data_store[w['name'].lower()] = w['id']
                    if w['name'].lower() == name:
                        return data,w['id']
                    print("\r{} indexing ..{} ".format(disp[ind],w['id']),end="")
                    ind+=1
                    ind%=4
                    data+=1
            return None,None
    data,id_ = find(sys.argv[1],data)
    print()
    print("the ID of the question is ",id_)
except KeyboardInterrupt:
    with open("data","w") as file:
        file.write(str(50*(data//50)))
else:
    with open("data","w") as file:
        file.write(str(50*(data//50)))

