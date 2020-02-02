import datetime 
import calendar 
  
date=input()
b= datetime.datetime.strptime(date, '%d %m %Y').weekday()
print(calendar.day_name[b])
