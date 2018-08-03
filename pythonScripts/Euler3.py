# What is the largest prime factor of the number 600851475143 ?

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

print(max(primefactorization(600851475143)))
        
