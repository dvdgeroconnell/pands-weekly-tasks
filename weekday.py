# weekday.py
# Week 05 assignment

# Program to output whether or not the current day is a weekday.
# If not a weekday, it also confirms that it is a weekend day.
# If neither, an error message is printed.

# Author: David O'Connell

# References
#   https://www.w3schools.com/python/python_datetime.asp - for date & time function syntax
#   (the datetime module has many methods to return information about the date object)
#   https://docs.python.org/3/reference/index.html - the Python Language Reference

# The method we require to return the current day is in the datetime module.
import datetime

# Define the weekdays and weekend days as tuples.
weekday = ("Monday","Tuesday","Wednesday","Thursday","Friday")
weekend = ("Saturday","Sunday")

today = datetime.datetime.now()

# The method strftime() formats date objects into readable strings.
# It takes one parameter to specify the format of the returned string.
# %A is the day of the week. Reference - W3schools.

# Check if today is a weekday.
if (today.strftime("%A")) in weekday:
    print("Yes, unfortunately today is a weekday.")

# If not a weekday, double check that it is a weekend day.
elif (today.strftime("%A")) in weekend:
    print("It is the weekend, yay!")

# If neither, print an error message. We should never get here.
else:
    print("I don't know what day it is!")
