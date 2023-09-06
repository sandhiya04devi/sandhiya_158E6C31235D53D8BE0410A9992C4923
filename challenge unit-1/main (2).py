def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 440 == 0:
    return True
  else:
    return False
year=int(input("Enter a Year : "))
if isLeapYear(year):
  print("{} is a Leap Year.".format(year))
else:
  print("{} is not a Leap Year.".format(year))