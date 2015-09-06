import pkg_resources
import __init__
working_directory = '/Users/ironstein/Documents/projects working directory/GRE/GRE codes/GRE final/final/'
__init__.__init__(working_directory)

from final_mark2.build import *
from final_mark2.build.build_list import build_word_list
from final_mark2.build.build_dictionary import build_word_dictionary
from final_mark2.run.run_time_functions import dictionary,test
from final_mark2.common.string_handling import words_from_string

working_directory_ = pkg_resources.resource_filename('final_mark2','working_directory')
working_directory_ = open(working_directory_,'w')
working_directory_.write(working_directory)
working_directory_.close()
del(working_directory_) 

LIST = []
DICTIONARY = {}

def setup() : 
	word_lists = ['common words 1', 'common words 2', 'common words 3', 'common words 4']
	include_words_list = [1,1,1,1]
	w = ''
	for word_list in word_lists : 	
		if include_words_list[word_lists.index(word_list)] is 1 : 
			words = pkg_resources.resource_filename('final_mark2.words',word_list)
			words = open(words,'r+')
			words_ = words.read()
			words.close()
			del(words)
			w += (words_) + '\n'

	return w

def main() : 

	global LIST 
	global DICTIONARY
	words = setup()
	LIST = build_word_list(words)
	DICTIONARY = build_word_dictionary(LIST)
	def get_input() : 
		function = input('what do you want to do ? ')
		if(function == 'dictionary') : 
			dictionary(LIST,DICTIONARY)
		elif(function == 'test') : 
			test(LIST,DICTIONARY)
		else : 
			print('function not available')
			get_input()

	get_input()

main()