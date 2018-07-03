import time
import webbrowser

while True:
#to get localtime
	timee = time.asctime()
#split time in day, date and year
	settime = timee.split()
#set condition for time
	if(settime[3] == '14:05:30'):
		print "Welcome"
#to open browser
#		webbrowser.open_new_tab("https://www.google.com")

		
