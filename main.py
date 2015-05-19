__author__ = 'Girish'

from scrapper.Snippet import Snippet
from scrapper.DataFinder import DataFinder
import json

import sys
if len(sys.argv) <2:
    print("Havent entered the name of the question")
# A trial application to get first 250 values
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
    datafetcher = DataFinder("http://www.spoj.com/problems/classical/sort=0,start={start}",start=data)
    html_snippet = Snippet(Snippet.SPOJ)
    d = 0
    for i in datafetcher.get_page():
        if d == 5:
            break
        for w in html_snippet.get_data_dicts(i):
            print(w)
            data+=1
        d += 1
except KeyboardInterrupt:
    with open("data","w") as file:
        file.write(str(data))
else:
    with open("data","w") as file:
        file.write(str(data))
