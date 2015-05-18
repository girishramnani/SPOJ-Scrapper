__author__ = 'Girish'


#contains the test for the utils file , basically the chache function

import unittest

from scrapper import Utils
class MyTestCase(unittest.TestCase):

    @Utils.time_it
    @Utils.cache("data")
    def basic_method(self,i):
        if i==0:
            return 0
        if i ==1:
            return 1
        return self.basic_method(i-1)+self.basic_method(i-2)

    def test_chache(self):
        self.assertEqual(self.basic_method(15),610)
        print(self.basic_method.elapsed)

    def test_shelf(self):
        import shelve
        t = shelve.open("data",writeback=True)
        print(t['1'])

    def test_file_present(self):
        import os
        self.assertTrue(os.path.isfile("data.bat"))

    def test_time_it(self):
        self.basic_method(20)
        self.assertGreater(self.basic_method.elapsed,0)

    # @classmethod
    # def tearDownClass(cls):
    #     import os,glob
    #     for file in glob.glob("data.*"):
    #         os.remove(file)
if __name__ == '__main__':
    unittest.main()
