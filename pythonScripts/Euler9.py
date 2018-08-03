##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

# abc has the form 500000*c-1000*c**2

#Euler's Theorem for Pythagorean Triples
# a == k(m**2-n**2)
# b == k(2*m*n)
# c == k(m**2+n**2)
# for some natural numbers m,n, k.
#m-n is odd, m,n coprime, m > n

# so a+b+c==1000 implies 2*m*k(m+n) == 1000
# so m*k(m+n) == 500

##Try k = 1 first

import math

m = 2

for m in range( math.ceil(math.sqrt(500))):
    n = 1
    for n in range(m):
        if m*(m+n)==500:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

print(a,b,c,a+b+c,a*b*c)

