# collatz.py
# Week 04 assignment 
# Ask the user to input a positive integer and apply the Collatz conjecture to it. The Collatz
# conjecture states that by applying 1 of 2 rules repeatedly, the number always reaches 4-2-1.
# 1. If the number is even, divide by 2
# 2. if the number is odd, multiply by 3 and add 1
# While no exceptions have been found, it has not been proven mathematically.
# 27 and 341 are good examples of how wildly the interim results can swing.

# Author: David O'Connell

# Reference(s)
#   https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#   https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

def sqrt(number, accuracy):
    curr_root = number/2
    delta = 1
    loop_count = 0
    while (abs(delta)) > accuracy:
        new_root = 0.5 * (curr_root + number/curr_root)
        delta = curr_root - new_root
        curr_root = new_root
        loop_count +=1
    print("Number of loops =", loop_count)
    return curr_root, delta

# main program

num = float(input("Enter a positive floating-point number, 0 to quit: "))

while (num < 0):
    num = float(input("Enter a positive floating-point number, 0 to quit: "))

if num != 0:

    desired_delta = float(input("Enter the delta at which iterations should stop: "))
    root, achieved_delta = sqrt(num, desired_delta)
    print("Square root of", num, "is", root, "with a final delta between iterations of", achieved_delta)
