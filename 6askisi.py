import datetime

year=int(raw_input('Enter Year:'))
month = int(raw_input('Enter Month:'))     
date = datetime.datetime(year, month, 1)
name_month = date.strftime('%B')

print name_month, year 
print "S\tM\tT\tW\tT\tF\tS"

for i in range(1,32):
	if date.month != month:
		break	
	if date.isoweekday() == 7:
		print "\n" +str(i), 
	elif date.day == 1:
		print "\n" + (date.isoweekday() * "\t") + str(i), 
	else:
		print "\t" +str(i),
	date += datetime.timedelta(days = 1)
     
