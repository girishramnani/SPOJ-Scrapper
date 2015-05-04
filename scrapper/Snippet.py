__author__ = 'Girish'

import re


class Snippet(object):

    def __init__(self,filter=None,**kwargs):

        if filter is None:
            statement =[r"(?P{}{})".format(key,val) for key,val in kwargs.items()]
            self.statement = "\n".join(statement)
            self.filter = re.compile(self.statement)
            self.spoj_filter=False
        else:
            self.filter = filter
            self.spoj_filter=True

    def __str__(self):
        return self.statement if not self.spoj_filter else "SPOJ filter"

    @classmethod
    def SPOJ(cls,data):
        result= re.finditer(r"""
        (?P<id><td[\s]* class\=\"text\-center\">\s*\d+\s*</td>)
        ([\s\w\=\<\"]*\>)
        (<a\s* href\=\"[\w/\.\:\"\s]*>)
        (?P<name>[\w\s\,]*)
        """,data,re.X|re.M)
        return result