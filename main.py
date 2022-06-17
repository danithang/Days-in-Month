def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      True
  else:
    False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #using function is_leap and pass in year to find which year is leap year and using month to figure out which month is February(2) to return 29 which is a leap year
    if is_leap(year) and month == 2:
        return 29
    #acts as else statement to return month_days variable and since lists starts at 0 the month - 1 makes the inputs start at 1st position
    return month_days[month - 1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












