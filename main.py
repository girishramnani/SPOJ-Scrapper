__author__ = 'Girish'


from scrapper.Snippet import Snippet
from scrapper.DataFetcher import DataFetcher



if __name__=="__main__":
    datafetcher = DataFetcher("http://www.spoj.com/problems/classical/sort=0,start={start}")
    html_snippet = Snippet(Snippet.SPOJ)
    d=0
    for i in datafetcher.get_page():
        if d ==5:
            break
        for w in html_snippet.get_data_dicts(i):
            print(w)
        d+=1
