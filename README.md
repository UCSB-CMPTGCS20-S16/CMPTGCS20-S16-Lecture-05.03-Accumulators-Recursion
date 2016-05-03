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

Misc Other
==========

To change your unix prompt to `'$ '` use:

```
export PS1='$ '
```
