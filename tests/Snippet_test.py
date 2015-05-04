__author__ = 'Girish'

import unittest

from scrapper import Snippet

class Snippet_test(unittest.TestCase):
    def test_constructor(self):
        Snippet.Snippet()

    def test_constructor_with_args(self):
        generated =Snippet.snippet(id="",title="")

    def test_contructor_with_args_and_filter(self):
        generated = Snippet.snippet(id=r"\d")
        generated.addFilter("title",r"[a-z]")

    def test_regex_with_one_arg(self):
        generated = Snippet.snippet(id=r"\d")
        self.assertEqual(generated,"(\d)")

    def test_regex_with_SPOJ_snippet(self):
        generated =Snippet.snippet(Snippet.SPOJ)
        self.assertEqual(generated,)









if __name__ == '__main__':
    unittest.main()
