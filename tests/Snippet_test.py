__author__ = 'Girish'

import unittest

from scrapper import Snippet

class Snippet_test(unittest.TestCase):
    def test_constructor(self):
        Snippet.snippet()

    def test_constructor_with_args(self):
        generated =Snippet.snippet(id="",title="")








if __name__ == '__main__':
    unittest.main()
