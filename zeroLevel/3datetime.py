"""In this Demonstration of datetime python library"""
import datetime 
currentDate = datetime.date.today()
# print(currentDate)
# print(currentDate.year)
# print(currentDate.month)
# print(currentDate.day)
# print(currentDate.strftime('%d %b %y %A %a %Y'))
# userInput = input ("Please enter your birthday (mm/dd/yyyy)")
# birthday  = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()

# print(birthday)
# days = birthday - currentDate
# print(days)
deadline = input("Enter deadline for Project:(mm/dd/yyyy) ")
day = datetime.datetime.strptime(deadline,'%m/%d/%Y').date()
daysleft = day - currentDate
nbrweeks = daysleft.days / 7
nbrdays = daysleft.days%7

print(daysleft)
print(nbrweeks)
print(nbrdays)