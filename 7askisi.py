import datetime
from datetime import date


START = datetime.datetime(date.today().year+1, 1, 1)
END = datetime.datetime(date.today().year+10, date.today().month, date.today().day)
count=0

date = START
while date <= END :
        if date.day == True and date.weekday() == True :
           count+=1
        date += datetime.timedelta(days=1)

print count

