"""
Exceptions

Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

"""



S = input()
try:
    print(int(S))
except ValueError:
    print("Bad String")
