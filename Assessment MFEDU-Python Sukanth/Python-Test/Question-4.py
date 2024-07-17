"""
Sum of digits of a number using recursion. Do it using recursion only.

Input: x = 123
Output: sum = 6

Input: x = 467
Output: sum = 17
"""

def sum_of_digits(x):
    if len(x) == 0:
        return 0
    sum_ = x[0] + sum_of_digits(x[1:])
    return sum_

x = input("Enter Num: ")
x = list(map(int, x))
print("Sum: ",sum_of_digits(x))
