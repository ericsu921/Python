#!/usr/bin/env python3

# ------------
# UnitTests.py
# ------------

# https://docs.python.org/3.2/library/unittest.html

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 0                                       # bug
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0                                # even when an internal assert is what stops the program from continuing, python's unittest does not get stopped and will run every tests
    return c

class MyUnitTests (TestCase) :                  # pythons unittest requires us to build our own class that extends the unittest's TestCase class
    def test_1 (self) :                         # must start with the word "test"
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" :
    main()

"""
FFF
======================================================================
FAIL: test_1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 25, in test_1
    self.assertEqual(cycle_length( 1), 1)
  File "./UnitTests.py", line 20, in cycle_length
    assert c > 0
AssertionError                                  # this failed due to an internal assertion failure, just a vanilla AssertionError, no details

======================================================================
FAIL: test_2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 28, in test_2
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6                          # this failed due to a unit test assertion failure, it even tells you what answer you got and what answer was expected

======================================================================
FAIL: test_3 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 31, in test_3
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=3)
"""
