#---------------------------------
# Lecture 5 Notes - error handling
#---------------------------------

""" Return Value """

def f(...) :
    ...
    if <something wrong>
        return -1
    ...

def g (...) :
    ...
    i = f(...)
    if i == -1 :
        <something wrong>
    ...

def h (...) :
    ...
    g(...)
    ...



# assumption: f will never return -1 for a good reason
# must always check if returned value is -1, if you're program is huge enough, you potentially have to check thousands of times




""" ======================================================= """




""" Global Flag"""

glob = 0

def f(...) :
    global glob             # must declare glob as global, otherwise glob will be local variable
    ...
    if <something wrong>
        glob = -1
        return 0
    ...

def g (...) :
    global glob
    ...
    i = f(...)
    if glob == -1 :
        <something wrong>
    ...

def h (...) :
    ...
    g(...)
    ...



# must always update global and check if global == -1, if you're program is huge enough, you potentially have to check thousands of times




""" ======================================================= """



""" Pass Value (v1.0) """

def f(..., loc2) :
    ...
    if <something wrong>
        loc2 = -1
    ...

def g (...) :
    ...
    loc = 0
    i = f(..., loc)
    if loc == -1 :
        <something wrong>
    ...

def h (...) :
    ...
    g(...)
    ...


# would not work, python passes by value, so loc and loc2 are two separate entities
# must pass something by address, in Java, primitive types are passed by value, Objects are not



""" ======================================================= """



""" Java """
class Test {
    static void f (..., Integer y) {
        y = -1;
    }

    static void g (...) {
        Integer z = new Integer(0);
        Integer x = 0;                  # autoboxing, automatically wraps the in 0 into an Integer object
        f(..., x);
        assert x == 0;
        # x would not be modified, even though it is passed by address. remember that Integers are immutable, so you would be building a brand new Integer and pointing x to that new Integer object.
        # we need 2 qualities, pass by address and mutable (same with Java and Python)
        # for Java, that's an array, for python, that's a lists
    }
}



""" ======================================================= """



""" Pass Value (v2.0)"""

def f(..., loc2) :
    ...
    if <something wrong>
        loc2[0] = -1
        return 0
    ...

def g (...) :
    ...
    loc = (0,)          # loc itself is not a tuple, its an address of a tuple somewhere in memory.
    i = f(..., loc)     # passing in the address to tuple
    if loc[0] == -1 :
        <something wrong>
    ...

def h (...) :
    ...
    g(...)
    ...


# will NOT work, tuples are immutable




""" ======================================================= """



""" Pass Value (v2.0) """

def f(..., loc2) :
    ...
    if <something wrong>
        loc2[0] = -1
        return 0
    ...

def g (...) :
    ...
    loc = [0]           # loc is now pointing to an address to a lists
    i = f(..., loc)     # passing in an address to list
    if loc[0] == -1 :
        <something wrong>
    ...

def h (...) :
    ...
    g(...)
    ...


# will work, lists are mutable

""" TWO REQUIREMENTS for this to work: """
# must be a by-address mechanism
# must be mutable



"""
DOWNSIDE TO THESE 3 MECHANISMS:

the user must be very responsible, must check everything, 
if the caller forgets to make that the change to the variable, 
then the program is misbehaving, we're just not noticing
its misbehavior until much later, and by that time we could be
far away from where the error first occurred.
"""




"""
if we do an assertion, the program stops and we can't keep
on going. 

we want something in the middle. we want f to call an 
exception. if we don't pay attention to that exception,
the program halts, but we can pay attention, handle the 
error, and off we go.
"""



""" ======================================================= """



""" Exception (v1.0) """

def f(...) :
    ...
    if <something wrong>
        raise E(...)            # E is a made up name
    ...

def g (...) :
    ...
    try :
        ...
        i = f(...)
        ...
    except E :                  # must match name on line 208
        <something wrong>
    ...

def h (...) :
    ...
    g(...)
    ...

# f raises E, doesn't do rest of f, doesn't do rest of try, does except block and is resolved

""" ======================================================= """




""" Exception (v2.0) """

def f(...) :
    ...
    if <something wrong>
        raise E(...)            
    ...

def g (...) :
    ...
    try :
        ...
        i = f(...)
        ...
    except E2 :                 # NOTICE doesn't match name on line 208
        <something wrong>
    ...

def h (...) :
    ...
    g(...)
    ...


# f raises E, doesn't do rest of f, doesn't do rest of try block, doesn't do except E2, because names don't match, goes to caller (h), no try-except block, goes to caller of h (not shown), and bubbles up to the top-level until it finds the except block of type E2, otherwise, program stops

""" 3 possibilities when raising an exception """
# - no try-except block, go to caller
# - there is a try-except block, but not of the one I raised, go to caller
# - there is a try-except block of which is the one I raised, the issue is resolved and off I go




""" ======================================================= """




# Exception (v3.0)

def f(...) :
    ...
    if <something wrong>
        raise E(...)            
    ...

def g (...) :
    ...
    try :
        ...
        i = f(...)
        ...
    except E :
        <something wrong>
    except E2 :
        ...
    else :                  # else clause runs if there is no exception raised.
        ...
    finally :               # finally ALWAYS runs. there's simply no way to not make it run. always runs last.
        ...
    ...

def h (...) :
    ...
    g(...)
    ...

# f raises E,  doesn't do rest of f, doesn't do rest of try, does except E block, resolves issue, doesn't do else because except was raised, ALWAYS does finally, does rest of g, continues normally.


""" ======================================================= """


""" Exception (v4.0) """

def f(...) :
    ...
    if <something wrong>
        raise E3(...)
    ...

def g (...) :
    ...
    try :
        ...
        i = f(...)
        ...
    except E :
        <something wrong>
    except E2 :
        ...
    else :                  # else clause runs if there is no exception raised.
        ...
    finally :               # finally ALWAYS runs. there's simply no way to not make it run. always runs last.
        ...
    ...

def h (...) :
    ...
    g(...)
    ...

# f isn't happy, raises an E3, don't do rest of f, don't do rest of try body, don't do either of except clauses, don't do else, always do the finally, don't do the rest of g, go to caller until you find the except E3 block, otherwise halt.
# long story short, when an exception is raised, stop everything and go to caller until you find the right except clause, while always doing the finally blocks.









