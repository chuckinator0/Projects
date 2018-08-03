##These methods are interesting to me because they show the structure
##of integers as composits of prime numbers. From here, you can explore
##ideas about greatest common factor, least common multiple, modular
##arithmetic, Rings and Fields, etc.  Math is fun! Numbers are the building
##blocks of the universe, and prime numbers are the building blocks of
##numbers.

import math

# The shortfactorization() method takes an integer as input
# and produces a list of the unique prime factors.
def shortfactorization(x):
    factors = []
    if x % 2 == 0:
        factors.append(2)
        x /= 2
    f = 3
    while f <= x:
        if x % f == 0:
            factors.append(f)
            x /= f
        f += 2
    if len(factors) == 0:
        factors.append(x)
    return factors

# The primefactorization() method takes an integer as input and produces
# a list of prime factors including multiplicity
def primefactorization(x):
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x /= 2
    f = 3
    while f <= x:
        while x % f == 0:
            factors.append(f)
            x /= f
        f += 2
    if len(factors) == 0:
        factors.append(x)
    return factors

#This method produces the nth triangular number.  This will be useful
# for implementing a program for counting the total number of divisors of
# an integer
def Triangle(n):
    return n*(n+1)/2

# This method will count the number divisors of an integer. I developed this
# using an idea from graph theory (complete graphs and complete subgraphs)
# which invokes the formula for triangular numbers.  I include an unfinished
# method to show that I am comfortable sharing a work-in-progress and am open
# to discuss ideas.
def countdivisors(j):
    count = len(shortfactorization(j)) # powers of prime factors are factors
    count += 1 #
    n = len(primefactorization(j))
    count += Triangle(n-1)
    for i in primefactorization(j):
        count -= Triangle(primefactorization(j).count(i)-1)
    
    return count

print(countdivisors(12))
print(primefactorization(12))
print(shortfactorization(12))
