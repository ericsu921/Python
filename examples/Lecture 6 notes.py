a = [2,3,4]		# list
print(type(a))	# list

a = [2]			# list of length 1

a = []			# list of length 0, empty

a = (2,3,4)		# tuple
print(type(a))	# tuple

a = (2)			# int, NOT tuple

a = (2,)		# tuple must include comma "," - ONLY weird one

a = ()			# tuple of length 0, empty

# parentheses are an unfortunate choice of delimiter. they are ambiguous.


""" ========================================================================== """


Integer i = new Integer(444747);
Integer j = new Integer(444747);
Integer k = i;

System.out.println(i == j);		# false
System.out.println(i.equals(j))	# true
System.out.println(i == k);		# true

# for java, "==" refers to identity, ".equals()" refers to content
# for python, "==" refers to content, "is (not)" refers to identity


""" ========================================================================== """


a = [2, 3, 4]
print(type(a))		# list

print(type(list))	# type, (makes sense, list is a type)

print(type(type))	# type


"""
In Java there are classes, we define a class, Class Foo, Java has define a bunch of classes
for me, like Class ArrayList. It turns out in Java, there's a class named Class. And you
and I can make instances of classes like ArrayList and Foo, but in Java you and I are not 
permitted to make instances of class Class. Nonetheless, instances of class Class are built,
and they are built in response, as a consequence of, defining a class. So when Java defines
class ArrayList, somebody magically builds an instance of class Class that describes that 
class. When you and I define class Foo, somebody magically builds an instance of class Class 
that describes class Foo. And you'd be delighted to know that when someone defined class Class, 
they built an instance of class Class to describe that. Those instances of class Class are 
repositories of information of the class that they're describing. So we can say to the class 
Class instance of class Foo, tell me Foo's methods, and it can tell me that.

Same story in Python. There are a bunch of types floating around: int, list, tuple...but what 
do these names actually mean? In Java they don't mean anything at runtime. In Java there is 
no meaning to "int" at runtime. "int" is just a compile notion allowing me to declare a 
variable of type int. But there's nothing "int" represents at runtime. With class Foo, how
exactly do we get at that class instance, at that class Class instance that describes class 
Foo? It's a bit funny, I actually have to say, Foo.class. Same goes for ArrayList, we have to 
say ArrayList.class.

Python made it prettier by having that exact same notion. If "int" and "list" and "tuple" is a 
type, python built a type named Type. Instances of type Type describe type int, list, tuple, etc. 
But here's the pretty thing. The name "int" "list" "tuple" is the name of the instance of 
type Type that describe that type. So when we say print(type(list)) what do you think it says?
type. The instance of type Type that describes list is named "list" and is of type "type." It
makes sense because list is called "list" and is a "type."

See Exception.py line 33 and 34.
"""



















