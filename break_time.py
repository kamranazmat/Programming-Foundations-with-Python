import webbrowser
import time

total_breaks = 3
count = 0
delay_time = 2*60*60
while count < total_breaks:
	time.sleep(delay_time)
	print ("Time now: " + time.ctime())
	webbrowser.open("https://www.youtube.com/watch?v=dKrVegVI0Us")
	count += 1
