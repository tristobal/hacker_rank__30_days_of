"""
Scope

Given A class constructor that takes an array of integers as a parameter and saves it to the instance variable.
A computeDifference method finds the maximum absolute difference between any numbers and stores it in the instance
variable.
"""


class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        max_ = max(self.__elements)
        min_ = min(self.__elements)
        self.maximumDifference = max_ - min_


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)