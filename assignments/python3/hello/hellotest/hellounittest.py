#!/usr/bin/env python3

# testing using unittest framework

import unittest
import sys

sys.path.append("..") # append parent folder into the system path

import hello
from hello import answer, greet

class HelloTest(unittest.TestCase):
    # optional - executes before runing test
    def setUp(self):
        print('Running unittest on hello module')

    def testAnswer(self):
        expect = "Hello World!"
        result = answer()
        self.assertEqual(expect, result)

    def testGreet(self):
        name = "World"
        expect = "Hello World!"
        result = hello.greet(name)
        self.assertEqual(expect, result)

    def tearDown(self):
        # optional - executes after all tests
        print('Done running unittest')


if __name__ == "__main__":
    unittest.main()