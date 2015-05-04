__author__ = 'Girish'


import shelve


def cache(filename):
    cache_memory = shelve.open(filename)
    def wrapper(f):
        def work(*args,**kwargs):
            data_received = f(*args,**kwargs)

