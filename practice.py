month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
print("Type in the year and month in format: year month and it will tell you how many days are in that month")
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    if month>12 or month<1:
        return "That month doesn't exist"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month-1]

year,month = input().split()

print(days_in_month(int(year),int(month)))