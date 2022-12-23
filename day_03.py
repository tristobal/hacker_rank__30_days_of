"""
Intro to conditional statements

Task
Given an integer, n, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format
A single line containing a positive integer, n.
"""

if __name__ == '__main__':
    N = int(input().strip())

    if 1 <= N <= 100:

        if N % 2 != 0:
            print("Weird")
        else:
            if 2 <= N <= 5:
                print("Not Weird")
            elif 6 <= N <= 20:
                print("Weird")
            elif 20 <= N:
                print("Not Weird")
