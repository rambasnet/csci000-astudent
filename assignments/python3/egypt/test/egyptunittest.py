#!/usr/bin/env python3

# testing using unittest framework

import unittest
import sys

sys.path.append("..") # append parent folder into the system path

import egypt

class Test(unittest.TestCase):
    # optional - executes before runing each test function
    def setUp(self):
        print('Running unittest on egypt module')
        self.input1 =  [8, 6, 10]
        self.input2 = [5, 4, 3]
        self.input3 = [5, 12, 13]
        self.input4 = [1, 2, 3]
        self.input5 = [2000, 100, 30000]

    def testAnswer1(self):
        expect = "right"
        result = egypt.answer(self.input1)
        self.assertEqual(expect, result)

    def testAnswer2(self):
        expect = "right"
        result = egypt.answer(self.input2)
        self.assertEqual(expect, result)

    def testAnswer3(self):
        expect = "right"
        result = egypt.answer(self.input3)
        self.assertEqual(expect, result)

    def testAnswer4(self):
        expect = "wrong"
        result = egypt.answer(self.input4)
        self.assertEqual(expect, result)

    def testAnswer5(self):
        expect = "wrong"
        result = egypt.answer(self.input5)
        self.assertEqual(expect, result)

    def tearDown(self):
        # optional - executes after each test function
        print('Done running unittest')

if __name__ == "__main__":
    unittest.main()