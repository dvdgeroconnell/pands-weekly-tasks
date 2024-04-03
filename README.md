# Repository - pands-weekly-tasks  
This is GitHub repository for the coursework associated with the Programming and Scripting module.  
 
| Author  | Student ID  | Term |  
|----------|---------|---------|  
| David O'Connell  | G00438912  | 1H 2024  |    

# Contents  

## Weekly Task 02 - bank.py
This program prompts the user to enter 2 amounts in cent, adds them and prints the
answer formatted as euro and cent. It avoids the use of floating point numbers as we
are dealing with currency.

## Weekly Task 03 - accounts.py
This program takes in a 10 character account number and outputs the account number with 
only the last 4 digits shown (and the first 6 digits replaced by X's).
The program is extended to deal with account numbers of any length. Assumptions are
stated.

## Weekly Task 04 - collatz.py
This program demonstrates the Collatz conjecture.
It asks the user to input a positive integer and applies the Collatz conjecture to it.
The Collatz conjecture states that by applying 1 of 2 rules repeatedly, the number 
always reaches 4-2-1.
1. If the number is even, divide by 2
2. if the number is odd, multiply by 3 and add 1

## Weekly Task 05 - weekday.py
This program outputs whether or not the current day is a weekday.
If not a weekday, it also confirms that it is a weekend day.
If neither, an error message is printed.

## Weekly Task 06 - squareroot.py
This program uses the Newton method to estimate the approximate square root of a positive
point number. It asks the user to specify the difference in the result between successive
iterations at which the loop should exit.
It prints the square root and accuracy (of the square), also the final delta between iterations.

## Weekly Task 07 - es.py
A program to read in a text file and print out the number of e's and E's it contains.   
It is assumed that both upper and lower case e's should be counted.  
3 functions were written to see which appeared most efficient.  
  - Read the whole file  
  - Read a line at a time  
  - Read a character at a time  

## Weekly Task 08 - plottask.py (and plottask_output.png)  
A program to display:  
- a histogram of a normal distribution of 1000 values with a mean of 5 and a std deviation of 2  
  truncated at 10  
- a plot of the function h(x) = x^3 in the range 0 - 10  
