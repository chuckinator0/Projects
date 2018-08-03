##What is the 10 001st prime number?

##def primefactorization(x):
##    factors = []
##    while x % 2 == 0:
##        factors.append(2)
##        x /= 2
##    f = 3
##    while f <= x:
##        while x % f == 0:
##            factors.append(f)
##            x /= f
##        f += 2
##    if len(factors) == 0:
##        factors.append(x)
##    return factors
##
##count = 1
##number = 3
##while count < 10001:
##    if len(primefactorization(number))==1:
##        count += 1
##        number += 2
##    else:
##        number += 2
##number -= 2
##
##
##print(number, count)

import math

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
                break
            elif n % (f+2) == 0:
                return False
                break
            f += 6
        return True

def PrimeCount(x):
    #this function outputs the xth prime number
    if x < 1:
        return 'Please input a positive number!'
    elif x == 1:
        return 2
    else:
        count = 1
        number = 3
        while count < x:
            if is_prime(number) == True:
                count += 1
                number += 2
            else:
                number += 2
        return number - 2

print(PrimeCount(10001))


        
            
            
        
