#!/usr/bin/env python3

# ----------------
# FunctionTuple.py
# ----------------

print("FunctionTuple.py")

def f (x, y, *z) :							# z is always going to be a tuple
    assert type(z) is tuple
    return [x, y, z]

def g (x, y, *z) :
    assert type(z) is tuple
    return [x, y, set(z)]

assert f(2, 3)       == [2, 3, ()]			# call with 2 args, get them back with an empty tuple
assert f(2, 3, 4)    == [2, 3, (4,)]		# you get to specify a number of required args, and when you say *z, and it will collect args you provide as a caller over and above the required args. note: you can only do the star once, and it's gotta be the last thing you do.
assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

t = (3, 4)
u = (2,)
assert t            == (3, 4)
assert t            != (4, 3)
assert f(2, t,  5)  == [2, (3, 4), (5,)]
assert f(2, 5,  t)  == [2, 5, ((3, 4),)]	# got a tuple of a tuple
assert f(2, 5, *t)  == [2, 5, (3, 4)]		# t gets unpacked and repacked
assert f(2, *t)     == [2, 3, (4,)]			# unpacked it and only one got repacked because the other was a required arg, and bc order matters for tuples, we know exactly which one will get repacked
assert f(*t)        == [3, 4, ()]			# both became required args
assert f(y = 3, *u) == [2, 3, ()]			# y by-name, x by unpacking *u
assert f(*u, y = 3) == [2, 3, ()]			# can swap order
#f(2, y = 5, *t)                          	# TypeError: f() got multiple values for argument 'y'...x by-pos, y by-name, then y by-unpacking again. no good.
#f(x = 2, y = 5, *t)                      	# TypeError: f() got multiple values for argument 'x'

l = [3, 4]
u = [2]
assert l            == [3, 4]
assert l            != [4, 3]
assert f(2, l,  5)  == [2, [3, 4], (5,)]
assert f(2, 5,  l)  == [2, 5, ([3, 4],)]
assert f(2, 5, *l)  == [2, 5, (3, 4)]
assert f(2, *l)     == [2, 3, (4,)]
assert f(y = 3, *u) == [2, 3, ()]
assert f(*u, y = 3) == [2, 3, ()]
#f(2, y = 5, *l)                          	# TypeError: f() got multiple values for argument 'y'
#f(x = 2, y = 5, *l)                      	# TypeError: f() got multiple values for argument 'x'

s = {3, 4}
u = {2}
assert s            == {4, 3}
assert s            == {3, 4}					# order doesn't matter
assert f(2, s,  5)  == [2, {3, 4}, (5,)]
assert f(2, 5,  s)  == [2, 5, ({3, 4},)]
assert g(2, 5, *s)  == [2, 5, {3, 4}]			# g() returns a list of the first two params but we made a set out of the optional args. unpacking set into optional args into the set
assert g(2, *s)     == [2, 3, {4}]       		# ?...we got lucky, we don't know the order so either one could become the required or the optional arg. could have been [2, 4, {3}]. when i actually try it, the order is always the same...interesting.
assert g(y = 3, *u) == [2, 3, set()]
assert g(*u, y = 3) == [2, 3, set()]
#g(2, y = 5, *s)                          # TypeError: f() got multiple values for argument 'y'
#g(x = 2, y = 5, *s)                      # TypeError: f() got multiple values for argument 'x'

d = {"b" : 4, "a" : 3}
u = {2 : "c"}
assert d                    == {'b' : 4, 'a' : 3}
assert d                    == {'a' : 3, 'b' : 4}				# order doesn't matter
assert f(2, d,  5)          == [2, {'a' : 3, 'b' : 4}, (5,)]
assert f(2, 5,  d)          == [2, 5, ({'a' : 3, 'b' : 4},)]
assert g(2, 5, *d.keys())   == [2, 5, {'a', 'b'}]
assert g(2, 5, *d.values()) == [2, 5, {3, 4}]
assert g(2, 5, *d.items())  == [2, 5, {('a', 3), ('b', 4)}]
assert g(2, 5, *d)          == [2, 5, {'a', 'b'}]
assert g(2, *d)             == [2, 'a', {'b'}]               # ?
assert g(y = 3, *u)         == [2, 3, set()]
assert g(*u, y = 3)         == [2, 3, set()]
#f(2, y = 5, *d)                                             # TypeError: f() got multiple values for argument 'y'
#f(x = 2, y = 5, *d)                                         # TypeError: f() got multiple values for argument 'x'
#f(**d)                                                      # TypeError: f() got an unexpected keyword argument 'a'

d = {"z" : 4, "y" : 3}				# bottom line: you cannot specify an optional param, you can only specify required params. it's perfectly fine to have a dictionary whose keys match the names of the params when you're doing the dict-unpacking but the name of that 3rd param that has a star in front of it, that is not a name that is available on the outside. that's why z doesn't count as a matching param name. we cannot specify anything about z by name from the outside bc z is a special param. the only one who knows about z is the function itself, which wasn't true of the required params x and y. so having z as a key in this dict is as severe as having some arbitrary key in this dict, which means there is no way we can unpack it and make the call to f() work.
#f(2, **d)             # TypeError: f() got an unexpected keyword argument 'z'
#f(**d)                # TypeError: f() got an unexpected keyword argument 'z'

d = {"y" : 3, "x" : 2}
#f(2, **d)                   # TypeError: f() got multiple values for keyword argument 'x'
assert f(**d) == [2, 3, ()]

d = {"y" : 3}
assert f(2,     **d) == [2, 3, ()]
assert f(x = 2, **d) == [2, 3, ()]
#f(**d)                             # TypeError: f() takes at least 2 arguments (1 given)

d = {"y" : 3, "t" : 5}		# t is not an param of f()
#f(2,     **d)         		# TypeError: f() got an unexpected keyword argument 't'
#f(x = 2, **d)         		# TypeError: f() got an unexpected keyword argument 't'
#f(**d)                		# TypeError: f() got an unexpected keyword argument 't'

print("Done.")
