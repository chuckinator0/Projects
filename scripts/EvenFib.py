# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million,
# find the sum of the even-valued terms.

Fibonacci = [1,1]
i = 0
while Fibonacci[i] < 4000000:
    Fibonacci.append(Fibonacci[i]+Fibonacci[i+1])
    i += 1

total = 0
for x in Fibonacci:
    if x % 2 == 0:
        total += x

print(total)
