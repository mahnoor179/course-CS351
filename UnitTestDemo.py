import unittest
from stat_func import median
class MedianTest (unittest.TestCase):
    def setUp(self):
        self.median_io =(([12,13,12,15,13,16,12],12),([1,2,1,2,3,4,3],None))
        print("Setup executed!")
    def testc(self):
        for (l, m) in self.median_io:
            self.assertEqual(median(1),m)
    def tearDown(self):
        self.median_io= None
        print("tearDown executed")
if __name__ == "__main__":
    unittest.main()
