"""
Nested Logic

Given the expected and actual return dates for a library book, create a program that calculates the fine (if any).
The fee structure is as follows:
- If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
- If the book is returned after the expected return day but still within the same calendar month and year
as the expected return date, fine = 15 Hackos x (the numbers of days late).
- If the book is returned after the expected return month but still within the same calendar year as the expected return
date, the fine = 500 Hackos x (the number of moths late).
- If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.


"""

YEAR = 2
MONTH = 1
DAY = 0

txt_date_expected = "9 6 2015"  # input()
array_date_expected = list(map(int, txt_date_expected.split()))

txt_date_actual = "6 6 2015"  # input()
array_date_actual = list(map(int, txt_date_actual.split()))

print(f"day = {array_date_expected[0]}, month = {array_date_expected[1]}, year = {array_date_expected[2]} (date returned)")
print(f"day = {array_date_actual[0]}, month = {array_date_actual[1]}, year = {array_date_actual[2]} (date due)")

fine = 0

if array_date_expected[YEAR] > array_date_actual[YEAR]:
    fine = 10000

if array_date_expected[YEAR] == array_date_actual[YEAR]:
    if array_date_expected[MONTH] > array_date_actual[MONTH]:
        fine += 500 * (array_date_expected[MONTH] - array_date_actual[MONTH])

    if array_date_expected[MONTH] == array_date_actual[MONTH]:
        if array_date_expected[DAY] > array_date_actual[DAY]:
            fine += 15 * (array_date_expected[DAY] - array_date_actual[DAY])

print(fine)
