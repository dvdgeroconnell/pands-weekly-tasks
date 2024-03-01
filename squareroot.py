# squareroot.py
# Week 06 assignment

# A program to take a positive floating-point number as input and output an approximation of its
# square root using the Newton method. The calculation is carried out in a function called sqrt().
# See the comments in the function sqrt() for details on how the Newton method is calculated.

# Author: David O'Connell

# Reference(s)
#   https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#   https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
#   https://docs.python.org/3/reference/index.html - the Python Language Reference


# This function calculates the approximate square root. It takes in the number and the delta at which
# point the iterations should stop.

def sqrt(number, reqd_delta):

    # Newton's method may be written as "for any number N, the square root is 0.5 * (X + N/X) where
    # X is the result of the previous iteration".
    # Start with an initial guess for X (X=N or X=N/2 are suggested) until the difference in X between
    # iterations is less than a specified delta.
    curr_root = number / 2
    delta = 1

    # Implement the calculation Root = 0.5 * (X + N/X) - iterate until the result has converged to within
    # the limit specified by the user.
    while (abs(delta)) > reqd_delta:
        new_root = 0.5 * (curr_root + number/curr_root)
        delta = curr_root - new_root
        curr_root = new_root

    # Return the final square root, the actual final delta between iterations, and the difference between
    # the original number and the calcuated root squared as a measure of the accuracy.
    gap = abs(curr_root**2 - number)
    return curr_root, delta, gap

#--------------------------------------------------------------------------------------------------------
# MAIN PROGRAM

# Read in the number for which the square root is required, cast to type float
num = float(input("Enter a positive floating-point number, 0 to quit: "))

# Check it is not negative or 0 and keep asking for a positive number (or 0 to quit)
while (num < 0):
    num = float(input("Enter a positive floating-point number, 0 to quit: "))

# Only find the root if the user has entered a positive float, otherwise if 0, exit
if num != 0:

    # Request the delta between subsequent approximate roots at which the iteration should stop 
    desired_delta = float(input("Enter the delta at which iterations should stop: "))

    # Find the root
    root, achieved_delta, accuracy = sqrt(num, desired_delta)

    # Print the results, including the approximate root, accuracy (on the square, not the root), and
    # the final delta between iterations when the required maximum delta was achieved   
    print("The square root of ", num, " is ", root, " with an accuracy (on the square) of +/-", accuracy, sep = "") 
    print("The final delta between iterations was", achieved_delta)
