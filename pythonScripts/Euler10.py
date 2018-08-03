##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.


#Sieve of Eratosthenes time!

import math

##
##PrimeList = list(range(2,2000000))
##
##i = 0
##while PrimeList[i] <= math.sqrt(2000000):
##    for x in PrimeList[i+1:]:
##        if x % PrimeList[i] == 0:
##            del PrimeList[PrimeList.index(x)]
##    i += 1
##
##print(sum(PrimeList))

# I need to find a way to make a running total of primes instead of storing them in a list.
# The above program is not efficient.

    
#hmm, let's try to get back to the sieve idea, this time building the sieve instead of carving
# it out of a huge list like the first time.



PrimeList = [2,3,5,7]
n = 11
total = 17
while n < 2000000:
    
    condition = True
    i = 0
    while i < len(PrimeList) and PrimeList[i] <= math.sqrt(n):
        if n % PrimeList[i] == 0:
            condition = False
            break
        i += 1
        
    if condition == True:
        PrimeList.append(n)
        total += n

    n += 2

print(total)


















    



