# bank.py
# A program that prompts the user to enter 2 amounts in cent,
# adds them and prints the answer formatted as euro and cent
# Author: David O'Connell

amount1 = int(input('Enter the first amount (in cent): '))
amount2 = int(input('Enter the second amount (in cent): '))

# the following calculation avoids possible inaccuracies introduced by floating point arithmetic
# the simpler calcuation [sum = (amount1 + amount2) / 100] is avoided
# read as integers the 2 amounts to be added

euro = (amount1+amount2) // 100
cent = (amount1+amount2) % 100

# concatenate and print the euro and cent parts of the final amount

print(f'The sum of these is €{euro}.{cent}')