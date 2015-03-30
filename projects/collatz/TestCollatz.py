#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase     # must import a couple of things from the unittest module, the class "TestCase" and the function "main"

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :          # must build our own class "TestCollatz" (can name w/e you want) and extend as our parent "TestCase" imported on line 14
    # ----
    # read
    # ----

    def test_read (self) :              # we now write our unit tests, the name must begin with the word "test" for it to participate in this test suite
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 1)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 1)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 1)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 1)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")      # we built a different input source, a python class called StringIO, they are both pretending to be, on the one hand, Strings, and on the other hand, input/output devices. for the input source r, we built it with a String.
        w = StringIO()                                          # output source
        collatz_solve(r, w)                                     # collatz_solve doesn't care where the input/output is coming from. in the test harness, we can then hard-wire the input source to a particular set of pairs and then exhibit an expectation of what the output better be.
        self.assertEqual(w.getvalue(), "1 10 1\n100 200 1\n201 210 1\n900 1000 1\n")    # write a test suite that is completely fine with the wrong answer so that it will pass. this is your starting point. write the tests first and don't worry about the correct answer just yet.
                            # ^ must call the function .getvalue(), which is a function defined in String IO, because a StringIO and a String are two completely different objects. there is in fact no definition of == with a stringIO on the left and a regular String on the right so it simply wouldn't work.
# ----
# main
# ----

if __name__ == "__main__" :         # this is like a guard that allows us to define the functions without automatically running the script.
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1         # coverage3 does not output to stdout, but rather to stderror, which is a different output device. 2>&1 is getting the redirection of output to not only impact stdout but to impact stderror. we're getting everything to end up in TestCollatz.out not only the output of the script but also the output of coverage3 which goes to stderror.



% coverage3 report -m                   >> TestCollatz.out              # >> means append to what is already in TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
