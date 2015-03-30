#!/usr/bin/env python3

# -------------
# Exceptions.py
# -------------

# https://docs.python.org/3.2/library/exceptions.html

def f (b) :                     # f takes in a boolean
    if b :
        raise NameError("abc")  # message "abc" within NameError exception
    return 0

print("Exceptions.py")

try :
    assert f(False) == 0        # f does not raise an exception so the except clause below never runs
except NameError :
    assert False                # asserting False shows that this line never runs, if it did, the program would stop, and the script would not have terminated normally

try :
    assert f(True) == 1         # the assert does not even run. an exception is thrown and it goes straight to the except clause.
    assert False                # this line does not run either
except NameError as e :         # this does run. I am guessing "e" is an alias an exception object? not sure.
    assert type(e)      is     NameError    # assure the type of this exception is NameError
    assert type(e.args) is     tuple        # shows that expections have a property called "args" of type tuple
    assert len(e.args)  ==     1            # this tuple is of length 1
    assert e.args       is not ("abc",)     # "is not" refers to identity, "==" refers to content. they are not the same tuple objects bc one of them is inside the exception object and we are building the other one on this line.
    assert e.args       ==     ("abc",)     # see line 11. this is a mechanism where you can stuff an exception object with a message, and then the person who's catching the exception can then read that message. to read the message, you must look at the args attribute.
else :
    assert False                # will not reach this because an exception was raise, "else:" only runs if an exception is not raised

assert type(NameError) is type
assert type(type)      is type

assert issubclass(NameError,     Exception)         # NameError has a child of Exception
assert issubclass(Exception,     BaseException)     # Exception has a child of BaseException
assert issubclass(NameError,     BaseException)     # NameError has a grandchild of BaseException, you can use issubclass to inquire about a grandparent class
assert issubclass(BaseException, object)            # like Java, python has a tree object system and object is the root of that tree. everything is of type object in some sense.

print("Done.")