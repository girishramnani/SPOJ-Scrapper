__author__ = 'Girish'

import unittest

from scrapper import Snippet

class Snippet_test(unittest.TestCase):
    def test_constructor(self):
        Snippet.Snippet()

    def test_constructor_with_args(self):
        generated =Snippet.Snippet(id="",title="")
        self.assertEqual(str(generated),"(?P<id>)(?P<title>)")

    def test_contructor_with_args_and_filter(self):
        generated = Snippet.Snippet(id=r"\d")
        self.assertEqual(str(generated),"(?P<id>\d)")

    def test_regex_with_SPOJ_snippet(self):
        generated =Snippet.Snippet(Snippet.Snippet.SPOJ)
        self.assertEqual(str(generated),"SPOJ filter")









if __name__ == '__main__':
    unittest.main()
