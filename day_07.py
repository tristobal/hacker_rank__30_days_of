"""
Arrays

Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Sample Input
4
1 4 3 2

Sample Output
2 3 4 1
"""

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = arr[::-1]
    print(" ".join(str(v) for v in res))
