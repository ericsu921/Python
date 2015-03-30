#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__" :					# this is a way of distinguishing whether we are running the script from the outside or whether we are inside the interpreter doing an import. typically when we're inside the interpreter doing an import, we are typically importing a script for the sake of defining a bunch of functions, not with the intention of running anything yet, and within the interpreter we decide which of the functions to run. but since this script has the indication of a function as a top level thing, we typically wouldn't want that to happen to being in the interpreter and saying import. it basically keeps this script from running when we import from the interpreter. instead of defining the functions AND running the executables, we just define the functions and it preps me to run the executables later.
    collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in 		# cat outputs the content of the file
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out 			# we want the program to get the input from the file, but we cannot tell the program do that from within the program, if we do, Sphere is not going to accept it because Sphere's waiting for the input to come from stdin, so in some sense, the program is expecting input from stdin, but the Linux OS allows us to fool the program into thinking its getting input from stdin, when in fact it's getting it from a file. using < and > we are doing a redirecting of IO, we are redirecting stdin using < and redirecting stdout using >



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the directory Collatz.html
"""
