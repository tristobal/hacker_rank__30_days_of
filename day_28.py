"""
RegEx, Patterns, and Intro to Databases

Consider a database table, Emails, which has the attributes First Name and Email ID. Given N rows of data simulating
the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.

Input Format
The first line contains an integer, N, total number of rows in the table.
Each of the N subsequent lines contains 2 space-separated strings denoting a person’s first name and email ID,
respectively.

Constraints
- 2 <= N <= 30
- Each of the first names consists of lower case letters [a – z] only.
- Each of the email IDs consists of lower case letters [a – z], @ and  only.
- The length of the first name is no longer than 20.
- The length of the email ID is no longer than 50.

Output Format
Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed
on a new line.
"""
import re

if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]

        x = re.search('@gmail.com', emailID)
        if x is not None:
            gmail_users.append(firstName)

    for user in sorted(gmail_users):
        print(user)
