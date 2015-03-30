#!/usr/bin/env python3

# --------
# Cache.py
# --------

print("Cache.py")

x = 2
y = 2 + 0
assert x is y	# x and y are the same

x = 257
y = 257
assert x is y	# they are same

x = 257            # cache: [-5, 256]
y = 257 + 0
assert x is not y	# as soon as you hit a 257, the int is big enough to where it is stored seperately, x starts becoming an address instead of an immutable int object
assert x ==     y
x -= 1
assert x is not y
assert x !=     y
y -= 1				# they small enough and are back to being integers 
assert x is y

x = -6				# cache: [-5, 256], same story at the other edge
y = -6 + 0
assert x is not y
assert x ==     y
x += 1
assert x is not y
assert x !=     y
y += 1
assert x is y

x = 2.34
y = 2.34
assert x is y

x = 2.34
y = 2.34 + 0
assert x is not y 	# two objects stored at different addresses
assert x ==     y

s = "abc"
t = "abc"
assert s is t 		# python also caches string literals

s = "abc"
t = "ab" + "c"
assert s is t 		# "i've seen this string before, i'm not going to build another one"

s = "abc"
u = "ab"
v = "c"
t = u + v
assert s is not t 	# if we put a couple of strings into string variables and then do the concatenation, python doesn't notice, we really had to go out of our way to fool python
assert s ==     t

a = []
b = []
assert a is not b 	# builds two brand new lists
assert a ==     b

a = ()
b = ()
assert a is b 		# doesn't build a brand new tuple, why do you want a new empty tuple, you can't change it anyway, they're immutable, you should be happy with one, not going to build you another one

a = set()
b = set()
assert a is not b 	# you get a new set
assert a ==     b

a = frozenset()
b = frozenset()
assert a is b 		# frozensets are immutable, not going to give you another one

a = {}
b = {}
assert a is not b 	# dictionaries are mutable, gives you a new one
assert a ==     b

print("Done.")