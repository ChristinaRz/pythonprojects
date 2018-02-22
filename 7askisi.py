from datetime import date, datetime


START = date.today().year+1
END = date.today().year+10
count=0


for year in range(START, END):
	for month in range(1,13):
		if datetime(year, month, date.today().day).weekday() == True:
			 count+=1
	
print count

