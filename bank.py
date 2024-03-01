# bank.py
# Week 02 assignment

# A program that prompts the user to enter 2 amounts in cent,
# adds them and prints the answer formatted as euro and cent

# Author: David O'Connell

# References:
#   https://docs.python.org/3/reference/index.html - the Python Language Reference
#   https://www.w3schools.com/python/ref_string_zfill.asp (for zfill)


# read as integers the 2 amounts to be added
amount1 = int(input('Enter the first amount (in cent): '))
amount2 = int(input('Enter the second amount (in cent): '))

# the following calculation avoids possible inaccuracies introduced by floating point division
# the simpler calcuation [sum = (amount1 + amount2) / 100] is avoided
# calculate the Euro amount
euro = (amount1+amount2) // 100

# add a leading zero if the total cent is less than 10
# use of zfill from https://www.w3schools.com/python/ref_string_zfill.asp
cent = str((amount1+amount2) % 100).zfill(2)

# concatenate and print the euro and cent parts of the final amount
print(f'The sum of these is €{euro}.{cent}')
