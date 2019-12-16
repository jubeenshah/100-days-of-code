# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month, day, year = map(int, input().split(" "))
def returnWeekday(month, day, year):
    weekDays = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    #print(month, day, year)
    return weekDays[calendar.weekday(year=year,month=month,day=day)]
print(returnWeekday(month, day, year))