__author__ = 'Girish'


import shelve


#methods not having a specific object association

def cache(filename):
    cache_memory = shelve.open(filename)
    def wrapper(f):
        def work(*args,**kwargs):
            data_received = f(*args,**kwargs)

    return wrapper


def time_it(function):
    import time
    time_elp = 0
    def work(*args):
        nonlocal time_elp
        ref_time = time.time()
        result= function(*args)
        time_elp+=(time.time()-ref_time)
        setattr(work,"elapsed",time_elp)
        return result

    return work