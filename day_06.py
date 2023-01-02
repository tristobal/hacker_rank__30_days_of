"""
Let's review

Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters
as 2 space-separated strings on a single line (see the Sample below for more detail).

Example
s = adbecf
Print abc def

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string, S.
"""
t = int(input())

strings = []
for i in range(1, t+1):
    s = input()
    strings.append(s)

for s in strings:
    first = []
    second = []

    for i in range(0, len(s)):
        if i % 2 == 0:
            first.append(s[i])
        else:
            second.append(s[i])
    print(f"{''.join(first)} {''.join(second)}")
