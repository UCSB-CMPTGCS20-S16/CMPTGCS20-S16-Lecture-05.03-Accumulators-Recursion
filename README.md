# CMPTGCS20-S16-Lecture-05.03-Accumulators-Recursion

# Why rewrite functions to compute min, max, sum, etc.

... when they are already built-in to Python?

```
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:54:16) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> x = [10,20,15]
>>> sum(x)
45
>>> min(x)
10
>>> max(x)
20
>>> 
```

* If you just want to solve a problem, you should NOT rewrite basic functions such as min, max, sum---use the built-in ones.
* On the other hand, if you are trying to LEARN HOW TO PROGRAM, these are great practice problems.

TWO APPROACHES:
==============

* Accumulators with for loops
* Recursion on lists

Rules for identifiers:

By identifiers, we mean:

* variable names
* function names
* later: class and method names
* module names (file name of something we are going to "import", with the .py on it.)


Two kinds of equals: = vs ==
----------------------------
```
x = y     
```

Makes x become a name for the value that y currently has.

```
x == y
```

Asks the question: do x and y refer to the same value?  The result of this is either `True` and `False`


Examples:

```
>>> 2 + 2 == 4
True
>>> 3 + 5 == -7
False
>>> x = 4
>>> 2 + 2 == x
True
>>> 5 = x
SyntaxError: can't assign to literal
>>> x = 7
>>> x == 7
True
>>> 7 == x
True
>>> 7 == 5
False
>>> 7 == x
True
>>> 5 == x
False
>>> 5 = x
SyntaxError: can't assign to literal
>>> 
```

Misc Other
==========

To change your unix prompt to `'$ '` use:

```
export PS1='$ '
```

NOTES FROM 05/05
================


Possibly a working version of myMin:

```Python
def myMin(someList):

    if type(someList)!=list:
        return False

    # we now know that someList is a list
    
    if someList==[]:
        return False

    # we now know that there is at least one element in the list
    # in other words: someList[0] exists!

    result = someList[0]  # initial assumption about the min

    for x in someList:
        if (x < result):
            result = x
    
    return result
```
