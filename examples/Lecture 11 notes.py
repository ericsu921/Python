b = [v ** 2 for v in a]			# list. produces a brand new container the size of a.
print(type(b))					# list

c = (v ** 2 for v in a)			# generator. produces a constant size object. need parentheses when standing alone, do not need then when passing into function as an arg.
print(type(c))					# generator

""" ============================================================== """

def f () :
	print "1"
	yield 2
	print "3"
	yield 4
	print "5"

x = f()
print(type(x))			# generator

# if yield is present in the definition of a function, then when you call the function, the function does not run, instead magic runs, and the magic that runs is the magic that produces a generator. when i get around to iterating over the result of the function, which is the generator, that's when the function starts running.

# when we call x = f(), the function does not run, but we can iterate over x

v = next(x)			# 1, yield is like return, yield is what will get stuck into v
print(v)			# 2, return will stop the function completely, but yield pauses the function, and waits for another call to next on the iterable, and it then starts where it left off until we exhaust the iterator

v = next(x)			# 3
print(v)			# 4

v = next(x)			# 5, no more yields, doesn't return anything, but instead has exhausted the iterator, the StopIteration exception is raised, and off we go

"""
yield allows a function to act as an iterable. that's pretty cool. the number of yield in the function is analogous to the number of elements in that iterable.
"""