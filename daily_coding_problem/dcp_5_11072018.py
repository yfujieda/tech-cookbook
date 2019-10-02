'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

'''
reference
https://gist.github.com/fadeev/1215910

def cons(a,b):
  return lambda m: m(a,b)

def car(cons):
  return cons(lambda a,b: a)

def cdr(cons):
  return cons(lambda a,b: b)
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons):
    return cons(lambda a, b: a)

def cdr(cons):
    return cons(lambda a, b: b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))