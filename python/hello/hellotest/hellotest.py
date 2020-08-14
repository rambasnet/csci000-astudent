#! /usr/bin/env python3

import sys

sys.path.append('..')
from hello import answer, greet

def testHello():
    assert answer() == "Hello World!"
    print('all test cases passed for answer()...')

def testGreet():
    name = "World"
    expect = "Hello World!"
    result = greet(name)
    assert expect == result
    assert greet('John') == 'Hello John!'
    assert greet('Jen') == 'Hello Jen!'
    print('all test cases passed for greet()...')

if __name__ == "__main__":
    testHello()
    testGreet()
    print('done testing...')
