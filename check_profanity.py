import urllib

def read_text():
	file = open("movie_quotes.txt")
	contents = file.read()
	#print contents
	check_profanity(contents)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	outout = connection.read()
	print (outout)
	connection.close()

read_text()