"""
Recursion

Develop a program that takes an integer input and then prints the factorial of that integer input on the output screen.
"""
import os


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()