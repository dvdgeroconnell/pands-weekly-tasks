# Weekly Task 03 - accounts.py

# Problem statement
    # Reads in a 10 character account number and outputs the account number with only the last 4 digits
    # showing (and the first 6 digits replaced by X's).
    # Extend the program to deal with account numbers of any length - state assumptions.

# Author(s): David O'Connell

# Reference for string functions, while loops and if statements - https://www.w3schools.com/python/

# Assign initial value to the account_no string
account_no =''

# It is assumed that an account number can be no longer than the IBAN standard of 34 alphanumeric
# characters minus the first 4 which are 2 country code and 2 check digits - so 30 maximum.
# It is also assumed that it should be digits only.

while (len(account_no) > 30 or (account_no.isdigit() == False and account_no != 'E')):
    account_no = str(input("Please enter a valid account number of no more than 30 digits, E to exit: "))

if account_no != 'E':
    # Create a copy of the account number, it is assumed the original will be required elsewhere
    hidden_account_no = account_no
    
    # Assign initial values to the required variables - probably overkill but old C habits die hard
    count = 0
    replace_string = ''

    # Build the string of X's to hide the initial X digits of the account number, where X = length-4
    while count < (len(hidden_account_no) - 4):
        replace_string += "X"
        count += 1

    # Build the original and replacement strings as required by the replace function
    digits_to_hide = hidden_account_no[0:len(hidden_account_no)-4]

    # Now do the replacement and print the result
    hidden_account_no = hidden_account_no.replace(digits_to_hide, replace_string)
    print(f"Account number is: {hidden_account_no}")

# Exit the program if 'E' was entered
elif account_no == 'E':
    print("Exiting...")