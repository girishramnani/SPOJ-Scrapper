__author__ = 'Girish'

import unittest
import requests
from scrapper.Snippet import Snippet

class Snippet_test(unittest.TestCase):

    def setUp(self):
        self.data = requests.get("http://www.spoj.com/problems/classical/")
        self.data = self.data.content.decode()
    def test_constructor(self):
        Snippet()

    def test_constructor_with_args(self):
        generated =Snippet(id="",title="")
        self.assertEqual(str(generated),"(?P<id>)(?P<title>)")

    def test_contructor_with_args_and_filter(self):
        generated = Snippet(id=r"\d")
        self.assertEqual(str(generated),"(?P<id>\d)")

    def test_regex_with_SPOJ_snippet(self):
        generated =Snippet(Snippet.SPOJ)
        self.assertEqual(str(generated),"SPOJ filter")

    def test_data_dict_yielder(self):
        generated =Snippet(Snippet.SPOJ)
        total = list(generated.get_data_dicts(self.data))
        total = list(generated.get_data_dicts(self.data))
        self.assertEqual(50,len(total))







if __name__ == '__main__':
    unittest.main()
