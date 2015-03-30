#!/usr/bin/env python3

from sys import stdin, stdout

def collatz_read (s) :  # s is a string
    return [int(v) for v in s.split()] # tokenizes s, turns each token into an int, and returns a list of those 2 things

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

def collatz_eval (i, j) :
    if i > j :
        i, j = j, i
    v = 0
    for n in range(i, j + 1) :
        c = cycle_length(n)
        if c > v :
            v = c
    return v

def collatz_print (w, i, j, v) :
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

def collatz_solve (r, w) :
    for s in stdin :                # going line by line through stdin
        i, j = collatz_read(s)      # calls read with the string that it got from stdin, parallel assignment to i and j
        v    = collatz_eval(i, j)   # shoves i and j into eval and assigns it to v
        collatz_print(w, i, j, v)

if __name__ == "__main__" :
    collatz_solve(stdin, stdout)
