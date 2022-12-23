"""
Loops

Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) should be printed on a new
line in the form: n x i = result.
"""

if __name__ == '__main__':
    n = int(input().strip())

    for i in range(10):
        x = i + 1
        print(f'{n} x {x} = {n * x}')