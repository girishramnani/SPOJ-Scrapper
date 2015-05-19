__author__ = 'Girish'


import shelve


#methods not having a specific object association

class cache(object):

    @classmethod
    def Cache(cls,filename):
        cls.cache_memory = shelve.open(filename)

    @classmethod
    def close(cls):
        cls.cache_memory.close()
    def __call__(self,f, **kwargs):
        def work(*args,**kwargs):
            name=str(args[1]) # as self would be the first one
            if name in self.cache_memory.keys():
                return int(self.cache_memory.get(name))
            data_received = f(*args,**kwargs)
            if type(data_received) == dict:
                self.cache_memory[data_received['name'].lower()]=data_received['id']
            else:
                self.cache_memory[name] = str(data_received)

            return data_received
        return work



def rcache(filename):

    """
    cache method for recursive methods
    :param filename:
    :return:
    """
    def wrapper(f):
        def work(*args,**kwargs):
            cache_memory = shelve.open(filename,writeback=True)

            name=str(args[1]) # as self would be the first one
            if name in cache_memory.keys():
                return int(cache_memory.get(name))
            data_received = f(*args,**kwargs)
            if type(data_received) == dict:
                cache_memory[data_received['name'].lower()]=data_received['id']
            else:
                cache_memory[name] = str(data_received)
            return data_received
        return work

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