"""
Dictionaries and Maps

Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. For each name queried,
print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for the name
is not found, print Not found instead.

"""
x = int(input())

dict_ = {}

for i in range(x):
    text = input().split()
    dict_[text[0]] = text[1]

while True:
    try:
        input_ = input()
        if input_ in dict_:
            print(f"{input_}={dict_[input_]}")
        else:
            print("Not found")
    except EOFError:
        break
