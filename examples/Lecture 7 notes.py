# Operators

i = 2
j = 3

k = (i << j)    # does << modify j? no. does it modify i? no. (i << j) simply produces an R-value.

k = (i + j)     # same story for the + operator

(i + j)         # doesn't make sense, you're spitting out a value into thin air

(i << j)        # same story, doesn't make sense

i += j          # does += modify j? no. does it modify i? yes. therefore, we can have it stand alone.

i <<= j         # same story

k = (i << 3)    # sure why not, (i << 3) produces an R-value which is then shoved into the L-value k

k = (2 << 3)    # also works, (2 << 3) also returns an R-value

2 <<= 3         # NOT okay, you cannot modify the literal 2, it's R-value, you can only modify an L-value

k = (i += 3)    # varies A LOT by language. in C, C++, Java, this would be fine bc in these languages, the += operator returns an R-value. in python, these operators (+=, -=, <<=, etc.) return NOTHING. so this is no good. they can ONLY stand alone.

(i += 3) = k    # this line is okay in C++, but not in C, Java, and obviously not in python

""" 
R-values are literals  and cannot be modified.
L-values are variables and can    be modified.
"""