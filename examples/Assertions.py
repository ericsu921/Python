#!/usr/bin/env python3

# -------------
# Assertions.py
# -------------

# https://docs.python.org/3.2/reference/simple_stmts.html#grammar-token-assert_stmt

def cycle_length (n) :          # python is typeless unlike java, you do not have to declare the type of a variable
    assert n > 0                # assert that the input is greater than 0
    c = 0 # should be c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)        # // is integer division, / is floating point division
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0                # assert that the output is greater than 0
    return c

print("Assertions.py")

assert cycle_length( 1) == 1    # the failure that resulted was the failure on line 18
assert cycle_length( 5) == 6    # whereas the failure for these two latter asserts resulted due to a wrong answer
assert cycle_length(10) == 7
                                # assertions are an awesome tool within a function. they are a horrible tool for testing. when an assertion fails inside a function, the script is going to halt and we are never going to run the rest of the tests. we want to write relatively large test suites with lots of tests in them and we wouldn't want one of those test to fail and stop the entire set of test, we want the test suite to keep on going.
print("Done.")

"""
% Assertions.py
Traceback (most recent call last):                          # Traceback will tell you the caller of the caller of the caller all the way to top level, very attractive
  File "./Assertions.py", line 23, in <module>              # tells us the file name, line number, calling context <module>, and the failed assertion
    assert cycle_length( 1) == 1
  File "./Assertions.py", line 18, in cycle_length          # tells us name of file, line number, name of function and the assertion that failed
    assert c > 0
AssertionError



% python -O Assertions.                                     # turns off all assertions, even the ones in lines 23-25, which is another reason why assertions are no good for testing.
Assertions.py
Done.
"""




"""
when you write a piece of code, you are producing an artifact that by nature has an incredibly high 
number of execution paths based on what the input is. so when you're testing your code before you
deliver it to somebody, you're doing your best to test all those possible execution paths and you
will always miserably fail at doing that. the best you'll ever do is test an incredibly minute 
fraction of those paths. but its the best that you can do and as you do it, some of those assertions
might fail, and you will of course fix the problem, write some more tests, run some more tests, 
maybe some other assertions will fail, you'll fix that, and so on. eventually you'll get to a point
we hope that none of your assertions are failing, and you're pretty confident that you're program is
as good as you can make it. of course you're not deluded into thing that you're program is bug free,
you're just confident that you're assertions are not failing. so now it's time to deliver your program
to a customer. and for a while, your customer is going to go down the exact same paths you went down,
and there isn't going to be a problem. the customer is going to use your program a bit longer, and 
they go without a doubt down a path that you never went down, but luckily you didn't make a mistake
on that path either. but it will come, without question, that they will go down a path you never went 
down on which you did make a mistake and the program will misbehave. they're going to call you up, say
the program is misbehaving. and what are you going to ask them? what'd you do? works for me! so 
clearly they're going to tell you some input that you obviously didn't try, and you're going to try
their input and of course for you your assertions are turn back on, and so luckily, some assertions
are going to fail, and in failing, isn't going to tell you a lot of information: the assertion that
failed, the name of the file, the number of the line, the name of the function. couldn't be further
ahead. if you do a shitty job on the assertions, isn't it clear that it misbehaves for you like it 
did for them and you will be no further ahead. but if you did a good job, then it's a fantastic 
tool.

now what we need to get crystal clear clarity about is what an assert is not appropriate for. it's
clearly not appropriate for testing because it will stop my test suite prematurely. it will also get
turned off when i do the optimization run. but the most important thing to appreciate about it is
that it's not appropriate for assertions to be used when you're trying to protect yourself against a 
user error. it is only appropriate for programmer errors.

assertions also act as a superior comment. it gives you insight on the programmers line of thinking
when writing the code, and it cannot go stale like a comment can due to the fact that it halt the
program if failing. you will be forced to keep these in some sense computable comments up-to-date.
"""




