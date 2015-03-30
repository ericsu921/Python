zip([2, 3, 4], [5, 6, 7]) => ([2, 5], [3, 6], [4, 7])		# takes the item at the same index and groups them together in an iterable. zip also produces an interable over which we iterate. 

zip([2, 3, 4], [5, 6]) => ([2, 5], [3, 6])		# zip will stop at the shorter of the two

zip([2, 3], [4, 5], [6, 7]) => ([2, 4, 6], [3, 5, 7])	# matrix transpose


""" ============================================================= """

# take in two values, take the difference, and square that difference
def sq_diff (x, y) :
	return (x - y) ** 2

print(sq_diff(2, 5)) => 9

def f (...) :
	...

f(sq_diff, ...)

# if we only call sq_diff once, it'd be kind of annoying to have to give it a name, just like if we need to use the int 52 just once, we wouldn't be required to stick it into a variable. we could just use it as a literal. just like you can build a literal of type int on the fly, you can also build a function on the fly using the keyword "lambda." this is called an anonymous function or a function literal.

f(lambda x, y : (x - y) ** 2, ...)		# function literals can only have one line, and it returns the result of that line automatically, no need for even a return statment.

sq_diff = lambda x, y : (x - y) ** 2	# equivalent to the line 11. there is nothing magical about the keyword "def" or the binding of the name sq_diff to that function. sq_diff is just a name and after doing sq_diff with def, no one stops me from doing sq_diff = 52. python doesn't care about that. here, we are reinstating the definition of sq_diff by using this anonymous function literal instead.

""" ============================================================= """

map(sqrt, [4, 9, 16]) => [2, 3, 4]		# produces a generator, just like zip and range, and it allows me to iterate over of a map. it applies a unary function on the elems of a single iterable and producing the result of calling that unary function on the elems of that one iterable.

map(add, [2, 3], [4, 5]) => [5, 9]			# will invoke a binary function bc we fed it two iterables, and it will invoke that binary function on the elems of the two iterables in lock step, items at the same index. isn't it obvious that map is related to zip. the result is in the form of a list, but in reality, it is not a list, it is an iterable.