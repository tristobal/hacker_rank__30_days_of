"""
2D Arrays
Develop a program that can take a 2d array as an input and then print the maximum hourglass sum of that array.

Context

A: 6 x 6
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in
A's graphical representation:
a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
"""

if __name__ == '__main__':

    arr = []
    max_hg = -9 * 7

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(0, 4):
        for j in range(0, 4):
            sum_ = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + \
                   arr[i + 1][j + 1] + \
                   arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            max_hg = sum_ if sum_ >= max_hg else max_hg

    print(max_hg)
