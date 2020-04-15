

# RULES FOR RECURSION
# 1. Must have a base case.
# 2. Must change state toward the base case.
# 3. Must call itself, recursively.

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total
​
​
​
# n! = n * (n-1)!
def factorial_r(n):
    if n <= 1:
        return 1
    return n * factorial_r(n-1)
​
​
factorial(5)
factorial_r(5)