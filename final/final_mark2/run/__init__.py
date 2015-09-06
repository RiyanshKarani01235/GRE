import sys
import os

def __init__(working_directory) : 
	print('inside __init__')
	sys.path.append(working_directory)
	os.chdir(working_directory)
