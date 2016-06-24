import os

def rename_files():
	files = os.listdir("/home/kamran/udacity_python/prank")
	# get current working directory
	path = os.getcwd()
	# change directory
	os.chdir("/home/kamran/udacity_python/prank")
	print ("Log:")
	for file in files:
		new_name = file.translate(None, "0123456789")
		print ("-------------------------------")
		print ("Old name: " + file)
		print ("New name: " + new_name)
		
		os.rename(file, new_name)
	os.chdir(path)

rename_files()