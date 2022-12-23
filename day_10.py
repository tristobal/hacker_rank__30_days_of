"""
Binary Numbers

Develop a program that can accept integer as an input and then convert it into a binary number and
then into in base 10 integer. We need to print the base 10 integer that denotes the maximum number of consecutive
1's in the binary representation of the input.

"""


if __name__ == '__main__':
    n = int(input().strip())
    bin_str = format(n, 'b')
    list_ones = (i for i in bin_str.split('0'))
    max_one = max(list_ones)
    print(len(str(max_one)))
