##What is the value of the first triangle number to have over five hundred divisors?
import math

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

def Triangle(n):
    return n*(n+1)/2

def countdivisors(j):
    count = 1 + len(shortfactorization(j))
    n = len(primefactorization(j))
    
    return count

##n = 1
##while countdivisors(Triangle(n)) < 500:
##    n += 1

print(countdivisors(12))
print(primefactorization(12))
print(shortfactorization(12))
