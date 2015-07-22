
import __init__
working_directory = '/users/ironstein/documents/projects working directory/gre/final'
__init__.__init__(working_directory)

import pkg_resources
from final_mark2.build import *
from final_mark2.build.build_list import build_word_list
from final_mark2.build.build_dictionary import build_word_dictionary

LIST = []
DICTIONARY = {}

def setup() : 

	words = pkg_resources.resource_filename('final_mark2.build','words')
	words = open(words,'r+')
	words_ = words.read()
	words.close()
	del(words)
	return(words_)

def main() : 

	global LIST 
	global DICTIONARY
	words = setup()
	LIST = build_word_list(words)
	DICTIONARY = build_word_dictionary(LIST)
	def get_input() : 
		function = input('what do you want to do ? ')
		if(function == 'dictionary') : 
			dictionary()
		else : 
			print('function not available')
			get_input()

	get_input()

def dictionary() :
	global LIST
	global DICTIONARY
	list_of_everything = LIST
	dictionary = DICTIONARY
	word_list = []
	for i in range(len(list_of_everything)) :
		word_list.append(list_of_everything[i][0][0])
	print(word_list)
	while(1) : 
		word = input('enter a word : ')
		if(word in word_list) :
			print_everything_about_word(word)
		elif(word == 'exit') :
			print('exiting')
			print('-----------------------------------')
			print()
			main()
		else :
			print('word not available')

def print_everything_about_word(word)  :
	#[word,figure_of_speech,meaning,clue,sentence,synonym,antonym,others,category]
	for i in range(len(LIST)) : 
		if(i == len(LIST)) : 
			print('no such word')
			break
		if(word == LIST[i][0][0]) : 
			word_array = LIST[i]
			if(len(word_array[2]) == 1) : 
				if(word_array[3] == ['']) :
					print(word_array[0][0] + '(' + word_array[1][0] + ')' + ' : ' + word_array[2][0])
				else : 
					print(word_array[0][0] + '(' + word_array[1][0] + ')' + ' : ' + word_array[2][0] + ' (clue : ' + word_array[3][0] + ')')
				print()

			else :
				print(word_array[0][0] + '(' + word_array[1][0] + ')' + ' : ' )
				for i in range(len(word_array[2])) : 
					if(word_array[3][i] == '') : 
						print(word_array[2][i])
					else : 
						print(word_array[2][i] + ' (clue : ' + word_array[3][i] + ')')
				print()

			if(word_array[4] != []) : 
				if(len(word_array[4]) == 1) :
					print('sentence : ' + word_array[4][0])
				else : 
					print('sentences :')
					for j in range(len(word_array[4])) :
						print(str(j+1) + '.' + word_array[4][j])
				print()

			if(word_array[5] != []) : 
				if(len(word_array[5]) == 1) :
					print('synonym : ' + word_array[5][0])
				else : 
					print('synonyms :')
					for j in range(len(word_array[5])) :
						print(str(j+1) + '.' + word_array[5][j])
				print()

			if(word_array[6] != []) : 
				if(len(word_array[6]) == 1) :
					print('antonym : ' + word_array[6][0])
				else : 
					print('antonyms :')
					for j in range(len(word_array[6])) :
						print(str(j+1) + '.' + word_array[6][j])
				print()

			# if(word_array[7] != [])
			# 	print('others :')
			# 	for strings in word_array[7] : 
			# 		print(strings)
			# 	print()

			if(word_array[7] != []) : 
				print('others : ')
				for strings in word_array[7] : 
					print(strings)
				print()

			if(word_array[8] != '') : 
				print('category : ' + word_array[8])

	print('------------------------')

main()