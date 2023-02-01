"""
Running Time and Complexity

Task
A prime is a natural number greater than 1 that has no positive divisors other than  and itself. Given a number, n,
determine and print whether it is Prime or Not prime.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up
with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code.
"""

t = int(input())
for _ in range(0, t):
    n = int(input())

    is_prime = False

    if n == 1:
        is_prime = True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = True
                break
    if is_prime:
        print("Not prime")
    else:
        print("Prime")
