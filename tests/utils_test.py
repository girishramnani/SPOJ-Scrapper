__author__ = 'Girish'


#contains the test for the utils file , basically the chache function

import unittest

from scrapper import Utils
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Utils.cache.Cache("data")


    @Utils.time_it
    @Utils.cache()
    def basic_method(self,i):
        z=1
        for z in range(1,i):
            z*=i
        return z

    def test_chache(self):
        self.assertEqual(self.basic_method(10000),99990000)


    def test_file_present(self):
        import os
        self.assertTrue(os.path.isfile("./data.dat"))


    def test_time_it(self):
        self.basic_method(10000000)
        self.assertLess(self.basic_method.elapsed,1)



if __name__ == '__main__':
    unittest.main()

