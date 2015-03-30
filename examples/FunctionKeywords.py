#!/usr/bin/env python3

# -------------------
# FunctionKeywords.py
# -------------------

print("FunctionKeywords.py")

def f (x, y, z) :
    return [x, y, z]

assert f(2, 3, 4) == [2, 3, 4]	# passing completely by-pos
#f(2, 3)                        # TypeError: f() takes exactly 3 args (2 given)
#f(2, 3, 4, 5)                  # TypeError: f() takes exactly 3 args (4 given)

assert f(2, z = 4, y = 3) == [2, 3, 4]	# passing partially by-pos, and partly by-name
#f(z = 4, 3, x = 2)                     # SyntaxError: non-keyword arg after keyword arg. NON-POSITION RULE, when you mix passing by-pos and by-name, by-pos has to come first
#f(2, z = 4, x = 2)                     # TypeError: f() got multiple values for keyword argument 'x'. x is already given a value by-pos
#f(2, z = 4, a = 5)                     # TypeError: f() got an unexpected keyword argument 'a'. There is no parameter named a

print("Done.")

# use-case: imagine you have a function that takes in 5 args, and you are in an ordinary language, and there 
# are hundreds of calls to that function, and a hundred thousand lines of code, don't all those calls look like, 
# number comma number comma number comma number. you have no idea what those 5 integers mean until you go and 
# look up the function. with passing args by-name, you can go up to each call and say, arg 1 equals, arg 2 
# equals, etc. and if you pass all by-name, order doesn't matter. downside: refactoring is a pain unless your IDE 
# does it automatically. once you change one name, every call to that function breaks. it's fragile.