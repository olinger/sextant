from webcam import *
from sun import *
from datetime import date,datetime,time,timedelta
from sync import *


s=sun(lat=42.727848,long=-73.690065)
today  = datetime.today().date() - timedelta(days = 1)
sunrise = datetime.combine(today, s.sunrise())
print("NOW: ", datetime.now())
print("Today's Sunrise: ", sunrise)

'''connect to webcam'''
cam = webcam('192.168.0.24', 'admin', '')

#cam.take_pic("test//", datetime.now().strftime('%m_%d_%y@%I_%M%p'))

'''connnect to dropbox'''
drop = sync()

times = []
while(True):
	if (today != datetime.today().date()):
		#day change, recalculate sunrise and moonrise
		sunrise =  datetime.combine(datetime.now().date(),s.sunrise())
		today = datetime.today().date()
		print(datetime.today().date())
		print(s.sunrise(),s.solarnoon(),s.sunset())
		times = [sunrise,sunrise+timedelta(minutes=180),sunrise+timedelta(minutes=60),sunrise+timedelta(minutes=80),sunrise+timedelta(minutes=100),sunrise+timedelta(minutes=120),sunrise+timedelta(minutes=140),sunrise+timedelta(minutes=160)]
		for time in times:
			print("Time ", str(time))
	index = 0
	for time in times:
		diff = (time - datetime.now())
		if(diff.total_seconds() < 30 and diff.total_seconds() > 0):

			name = datetime.now().strftime('%I_%M%p')
			today = datetime.today().date()

			directory =  str(today)+'/'
			ext = ".jpg"
			fullname = directory + name + ext

			cam.take_pic(directory, name)
			drop.uploadfile(fullname, False)

			del times[index]
			index = index-1

		index = index+1
			

#if either moon or sunrise, snap pic, put in correct folder