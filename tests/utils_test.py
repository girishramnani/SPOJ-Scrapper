__author__ = 'Girish'


#contains the test for the utils file , basically the chache function

import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

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


    def test_time_it(self):
        self.basic_method(10000000)
        self.assertLess(self.basic_method.elapsed,4)

    @classmethod
    def tearDownClass(cls):
        Utils.cache.close()
        import glob
        import os
        for file in glob.glob("data.*"):
            os.remove(os.path.abspath(file))

if __name__ == '__main__':
    unittest.main()

