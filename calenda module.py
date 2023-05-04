# we are trying to print the day of the week of a given date. The date format is M/D/Y
# there's a weekday() function within the calendar module for this tasks
# we need to use the input data as args for the weekday() function
# when a string such as 05 is converted using the int() method, the 0 is removed
# this function returns the day of the week as an index, eg 0 for Monday and 1 for Tuesday
import calendar
date = input().split()
days_of_the_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
month, day, year = int(date[0]), int(date[1]), int(date[2])
print(days_of_the_week[calendar.weekday(year, month, day)])