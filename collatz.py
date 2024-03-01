# collatz.py
# Week 04 assignment 

# Ask the user to input a positive integer and apply the Collatz conjecture to it. The Collatz
# conjecture states that by applying 1 of 2 rules repeatedly, the number always reaches 4-2-1.
# 1. If the number is even, divide by 2
# 2. if the number is odd, multiply by 3 and add 1
# While no exceptions have been found, it has not been proven mathematically.
# 27 and 341 are good examples of how wildly the interim results can swing.

# Author: David O'Connell

# References
#   https://www.youtube.com/watch?v=094y1Z2wpJg&t=1 - more information on the Collatz conjecture
#   https://docs.python.org/3/reference/index.html - the Python Language Reference

# ask the user for the number to apply the Collatz conjecture to and cast to int
entry = int(input("Input a positive integer: "))

# test whether even or odd by looking at the remainder, and apply rule 1. or rule 2. accordingly
# remain in the loop until the number has reached 1
while entry != 1:
    if entry % 2 == 0:
        # apply rule 1.
        entry = entry / 2
    else:
        # apply rule 2.
        entry = (entry * 3) + 1
    
    # print the result of each step
    print(int(entry), end = ' ')