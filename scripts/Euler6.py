# Find the difference between the sum of the squares of the
#first one hundred natural numbers and the square of the sum.

def sumofsquares(n):
    # formula for sum of first n square numbers
    total = n*(n+1)*(2*n+1)/6
    return total
def GaussSum(n):
    # formula for sum of first n natural numbers
    total = n*(n+1)/2
    return total


print(sumofsquares(100) - GaussSum(100)**2)

