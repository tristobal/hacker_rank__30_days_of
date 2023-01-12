"""
Exceptions

Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

"""


# TODO This line must be REMOVED (not commented) in order to pass the tests
# if __name__ == '__main__':
S = input()
try:
    print(int(S))
except ValueError:
    print("Bad String")
