# Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
b = 999
BigPali = 0
x = a*b

while a > 100:
    while b > 100:
        x = a*b
        if str(x) == str(x)[::-1] and x > BigPali and x % 11 == 0:
            BigPali = x
        b -= 1
    a -= 1
    b = 999

print(BigPali)
