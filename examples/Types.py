#!/usr/bin/env python3

# --------
# Types.py
# --------

import sys
from types import FunctionType

print("Types.py")

assert type(type) is type
assert issubclass(type, type)           # every class is a subclass of itself, another curiosity of the function issubclass()
assert issubclass(type, object)         # every class is a subclass of object

b = True
b = False
assert type(b)    is bool
assert type(bool) is type
assert issubclass(bool, bool)
assert issubclass(bool, object)

i = 2                                   # for ints in python, there is no underbound or overbound overflow machinery of any kind, which clearly exists in both Java and C++. these are indefinite precision integers, so as many integers as memory can hold is what it will take
assert type(i)   is int
assert type(int) is type
assert issubclass(int, int)
assert issubclass(int, object)

assert issubclass(bool, int)            # bool and int seem to be related which is another curiosity, it is not obvious to me that that would be true. in this case, bool is a child of int

f = 2.3                                 # this no doubt does have limits to its values, these are not indefinite precision values
assert type(f)     is float
assert type(float) is type
assert issubclass(float, float)
assert issubclass(float, object)

c = 2 + 3j                              # complex numbers, real and imaginery parts of a complex number
assert type(c)       is complex
assert type(complex) is type
assert issubclass(complex, complex)
assert issubclass(complex, object)

s = 'abc'                               # '' or "", you can then put a string inside of a string without having to escape the delimiter, in Java you have to do "Mike says \"hello\" from Austin" to get, Mike says "hello". in python you can just say "Mike says 'hello' from Austin"
s = "abc"
assert type(s)   is str
assert type(str) is type
assert issubclass(str, str)
assert issubclass(str, object)

l = [2, "abc", 3.45]        # list - can be heterogeneous
assert type(l)    is list   # (1) mutable, (2) order matters, (3) allows duplicates, (4) implemented with internal array, (5) items can be anything
assert type(list) is type
assert issubclass(list, list)
assert issubclass(list, object)

t = (2, "abc", 3.45)        # tuple, same heterogeneity
assert type(t)     is tuple # effectively immutable lists
assert type(tuple) is type
assert issubclass(tuple, tuple)
assert issubclass(tuple, object)

s = {2, "abc", 3.45}        # set, again, heterogeneous
assert type(s)   is set     # (1) mutable, (2) order does NOT matter, (3) does NOT allow duplicates, (4) internal hashtable (5) items must be "hashable" and therefore immutable. for a list, all that needs to be define is equality. when you traverse through the list, you need to compare each elem to the elem you are looking for and ask are they equal? a set could be implemented with an internal tree (like a TreeMap is in Java). trees, on the other hand, need some ordering/comparison mechanism in order to find the desired elem. a set could also be implemented with an internal hashtable (like a HashMap is in Java). hashtables need a hash function, and the items you put in the set must be "hashable", and only immutable objects are hashable. a set is not immutable, so you cannot have a set of sets, but it CAN have a set of frozen sets (which are immutable and therefore hashable). a frozen set is just an immutable set, just like a tuple is in some sense just an immutable list. so in some sense, a set IS a hashset in python. sets are implemented with a hashtable, not with a tree.
assert type(set) is type
assert issubclass(set, set)
assert issubclass(set, object)

d = {2 : "def", 3.45 : 3, "abc" : 6.78}     # dictionary, again, heterogeneous. similar to Java's HashMap/TreeMap. python uses hashes to implement the dict
assert type(d)    is dictionary             # key-value pairs, only keys need to be hashable, values can be anything. lookup of key is O(1), lookup of value is O(n). python just needs equality to be defined on keys, nothing special about looking up values. strings are hashable because strings are immutable.
assert type(dict) is type
assert issubclass(dict, dict)
assert issubclass(dict, object)

class A :                           # built our own type named A. aside: the keyword "class" doesn't have a meaning, just like "def" does not have a meaning. it's just an introducer. in Java, there's a data member named "class" of all classes that are built either by you or by Java, which is invoked using <ClassName>.class. the keyword "class" by itself doesn't have any meaning in Java either.
    def __init__ (self, i, f) :     # analogous to Java's constuctor. "self" in python is like "this" in Java. in python, you must include "self" as an arg of the __init__ function (not sure if you need to for all functions...), whereas in Java, you don't have to specify this as an arg, but you can still make use of it in the body, just like we can make use of self in the body of a python constructor. this gets called when you make an instance of this class.
        self.i = i                  # without saying "self.i", you would be building a local var named i. here, we are creating an instance variable.
        self.f = f                  # in Java, we would "declare" our data members OUTSIDE of my methods/constructors and then my constructors job in Java would be to "initialize" these data members. in python, the constructor is making the data members come into "existence" in addition to initializing them. they both create AND define vars in the method __init__. if we declare a var outside of a method, that's python's notion of a class var. in Java we would need to invoke the keyword "static." in python, just the existence of it outside a method will make it a class data member.

x = A(2, 3.45)                      # we build a new instance of A
assert type(x) is A                 # x is of type A
assert type(A) is type              # A must be a type
assert issubclass(A, A)
assert issubclass(A, object)        # all classes stem as subclasses from object

class B (A) :                       # B extends A as a parent class
    def __init__ (self, i, f, s) :  # B adds another var s
        A.__init__(self, i, f)      # have B's constructor invoke A's constructor. this line in python is not required. python exhibits replacement overriding. replacement overriding says that the child's definition is going to replace the parent's definition. refinement overriding says that the child's defintion refines the parent's definition, which means that the child's definition is absolutely obligated to call the parent's definition first and then it can do more stuff. Java exhibits refinement overriding. in Java, a child's constructor must ALWAYS call its parent's constructor first. even if we say nothing in the child's constructor, it will invoke the parent's default constructor. if the parent doesn't not have a default constructor, it wouldn't compile. we can use they keyword "super" to invoke one of the parent's non-default constructors. but the child's constructor is obligated, in one way or another, to invoke the parent's constructor. nothing else in Java exhibits refinement overriding. if a child class overrides a parent class's method, no one is twisting our arm to also call the parent's version of that method. we can still do it but we don't have to. everything outside of constructors in Java exhibit replacement overriding. Python exhibits replacement overriding for its constructors. it does not force the child constructor to call parent's constructor. in this line, we chose to do call the parent on our own. we could have chosen not to. however, without this line, something curious would happen. i and f wouldn't be defined. we could call A's methods, which may depend on A's data, which we would not have, and things would not go well. furthermore, python is extremely dynamic in comparison to Java. in Java, when we define a class and the data members within it, all instances of that class will have exactly that set of data, no more, no less, forever. but in python, data members are created by invoking a certain method, (which includes the __init__ method. there's nothing particularly special about the constructor other than the fact that it gets called when we first build the object). well, we can write some other method in python and that method can define some new data for our class. that means that if we define a class in python, and we build instances of that class, depending on what methods we invoke on each of those instances, each of those instances could have a different set of data. and after the instance already exists, we can still change its set of data. so over time that instance can change what data it has, and all instances of the same class may have different data members.
        self.s = s

y = B(2, 3.45, "abc")
assert type(y) is B
assert type(B) is type
assert issubclass(B, B)
assert issubclass(B, object)

assert issubclass(B, A)

def inc (v) :                                   # defines a function, (not a method, methods are defined inside a class)
    return v + 1
assert type(inc)          is FunctionType       # nothing special about functions, they're just objects of type FunctionType
assert type(FunctionType) is type
assert issubclass(FunctionType, FunctionType)
assert issubclass(FunctionType, object)

print("Done.")
