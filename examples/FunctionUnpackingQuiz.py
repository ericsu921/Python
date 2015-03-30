#!/usr/bin/env python3

# --------------------
# FunctionUnpacking.py
# --------------------

""" Comment out all illegal function calls """

import collections

print("FunctionUnpacking.py")

def f (x, y, z) :
    return [x, y, z]

t = (3, 4)                   
f(2, t, 5)   
f(2, 5, t)   
f(2, *t)     
f(z = 2, *t) 
f(*t, z = 2) 
f(*t, 2)     
f(x = 2, *t) 
f(*t)        
f(2, 5, *t)  

l = [3, 4]
f(2, l, 5)   
f(2, 5, l)   
f(2, *l)     
f(z = 2, *l) 
f(*l, z = 2) 
f(*l, 2)     
f(x = 2, *l) 
f(*l)        
f(2, 5, *l)  

s = {3, 4} 
f(2, s, 5)        
f(2, 5, s)        
set(f(2, *s))     
set(f(z = 2, *s)) 
set(f(*s, z = 2)) 
f(*s, 2)          
f(x = 2, *s)      
f(*s)             
f(2, 5, *s)       

d = {"b" : 4, "a" : 3}
type(d.keys()) is not collections.KeysView
isinstance(d.keys(), collections.KeysView)
set(d.keys()) 

type(d.values()) is not collections.ValuesView
isinstance(d.values(), collections.ValuesView)
set(d.values()) 

type(d.items()) is not collections.ItemsView
isinstance(d.items(), collections.ItemsView)
set(d.items()) 

f(2, d, 5)
f(2, 5, d)             
set(f(2, *d.keys()))   
set(f(2, *d.values())) 
set(f(2, *d.items()))  
set(f(2, *d))          
set(f(z = 2, *d))      
set(f(*d, z = 2))      
f(*d, 2)               
f(x = 2, *d)           
f(*d)                  
f(2, 5, *d)            
f(2, **d)              

d = {"z" : 4, "y" : 3, "x" : 2}
f(2, **d)
f(**d) 

d = {"z" : 4, "y" : 3}
f(2,     **d) 
f(x = 2, **d) 
f(**d, 2)     
f(**d, x = 2) 
f(**d)        
f(2, 5, **d)  

d = {"y" : 3}           
f(2, 4, **d)     
f(2, z = 4, **d) 

d = {"z" : 4, "y" : 3, "t" : 5}
f(2,     **d) 
f(x = 2, **d) 
f(**d)        

t = (2, 3)
d = {"z" : 4}
f(*t, **d) 
f(**d, *t) 

print("Done.")