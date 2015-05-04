__author__ = 'Girish'

import requests

import re
test = requests.get("http://www.spoj.com/problems/classical/")
data = test.content.decode()
print(data)
data= re.sub("[\\n\\t]+","",data)

#for understand the regex for html
result= re.findall(r"""
    <title>[\w\s\(\)\-]*</title>
""",data,re.X|re.M)

#regex for SPOJ
result2= re.finditer(r"""
    (?P<id><td[\s]* class\=\"text\-center\">\s*\d+\s*</td>)
    ([\s\w\=\<\"]*\>)
    (<a\s* href\=\"[\w/\.\:\"\s]*>)
    (?P<name>[\w\s\,]*)
""",data,re.X|re.M)
for match in result2:
    print(match.groupdict())

