import pkg_resources
import random
import time

from final_mark2.common.string_handling import *
from final_mark2.run.directory_handling import is_file_in_directory

working_directory = pkg_resources.resource_filename('final_mark2','working_directory')
working_directory = open(working_directory)
working_directory_ = working_directory.read()
working_directory.close()
working_directory = working_directory_

del(working_directory_)
print(working_directory)

other_log_file = 'android_test_log'
global LIST
global DICTIONARY

def dictionary(_list_,dictionary) :
	global LIST
	global DICTIONARY
	LIST = _list_
	DICTIONARY = dictionary

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
		else :
			print('word not available')

def test(_list_,dictionary) : 

	global LIST
	global DICTIONARY
	LIST = _list_
	DICTIONARY = dictionary

	not_answered_words = _list_
	answered_words = []

	review = pkg_resources.resource_filename('final_mark2.words','review words')
	
	already_wrong_words = []
	already_wrong_words_count = []

	def write_to_review(string_) :
		already = '' 
		with open(review,'r') as r:
			already += r.read()
		with open(review,'w') as r : 
			r.write(already)
			if string_ not in already_wrong_words : 
				already_wrong_words.append(string_)
				already_wrong_words_count.append(0)
				r.write(string_)
				r.write('\n')
			else : 
				already_wrong_words_count[already_wrong_words.index(string_)] = 0
	
	write_to_review('------------  ' + time.strftime('%x') + '  ' + time.strftime('%H:%M:%S') + '  ------------')

	def test_one_word() : 

		print('--------------------  ' + str(len(not_answered_words)) + '  --------------------')

		random_word_index = random.randint(0,len(not_answered_words)-1)
		random_word = not_answered_words[random_word_index]
		print(random_word[0][0])

		def get_input(string) : 
			try : 
				_input = input(string)
			except TypeError : 
				return get_input(string)
			if _input is 'y' : 
				return False
			if _input is 'n' : 
				return True
			else : 
				return get_input(string)

		input_ = input('press enter to see the meaning ')
		print('the answer was : ' + str(random_word[2]))
		# answered_words.append(not_answered_words.pop(random_word_index))
		_input = get_input('did you know the meaning of this word ? y/n ')
		# print(_input)
		if(not _input) : 
			# print('y pressed be ')
			# print('the answer was : ' + str(random_word[2]))
			if random_word[0][0] in already_wrong_words : 
				if already_wrong_words_count[already_wrong_words.index(random_word[0][0])] is 3 :
					answered_words.append(not_answered_words.pop(random_word_index))
				else : 
					already_wrong_words_count[already_wrong_words.index(random_word[0][0])] += 1
			else : 
				answered_words.append(not_answered_words.pop(random_word_index))

		else :
			write_to_review(random_word[0][0])
			empty_list = [[],'',['']]
			if random_word[3] in empty_list : 
				print('hint not available')
			else : 
				print('hint :',str(random_word[3]))

		# print('----------------------------------------------------')

	while len(not_answered_words) is not 0 : 
		test_one_word()
	for i in range(3) : 
		print()
		
	print('+-----------------------------------------------------------------+')
	print('|                                                                 |')
	print('|          CONGRATULATIONS, YOU HAVE COMPLETED THE TEST           |')
	print('|                                                                 |')
	print('+-----------------------------------------------------------------+')

		# print(len(not_answered_words))

	# def get_input() : 
	# 	answer = input('do you want to merge the two log files ? ')
	# 	if(answer == 'yes') : 
	# 		return True
	# 	elif(answer == 'no') : 
	# 		return False 
	# 	else : 
	# 		print('invalid response, please try again')
	# 		return(get_input())

	# global LIST
	# global DICTIONARY
	# LIST = _list_
	# DICTIONARY = dictionary
	# test_log = open('test_log','r+')
	# test_log_ = test_log.read()
	# test_log.close()
	# test_log = test_log_
	# del(test_log_)
	# if(is_nothing_in_file(test_log)) : 
	# 	print('building empty log ...')
	# 	build_empty_log()
	# if(is_file_in_directory(other_log_file,working_directory)) :
	# 	print('android test log also present')
	# 	log_file = is_file_in_directory(other_log_file,working_directory)
	# 	print(log_file)
	# 	answer = get_input()
	# 	if(answer) : 
	# 		print('merging log files ...')
	# 		#merge_log_files(log_file)
	# 		#after merging log files, delete the android_test_log
	# 	else : 
	# 		print('merging aborted')

	# else : 
	# 	print('android test log not found')

def build_empty_log() : 
	word_list = []
	test_log = pkg_resources.resource_filename('final_mark2.run','test_log')
	test_log = open(test_log,'w')
	test_log.write('{0:15s}{1:10s}{2:10s}{3:10s}\n'.format('name','correct','wrong','last session score\n'))
	for word_array in LIST : 
		test_log.write('{0:15s}{1:10s}{2:10s}{3:10s}\n'.format(word_array[0][0],'0','0','0'))
	test_log.close()

def is_nothing_in_file(string) : 
	i = 0
	if(len(string) == 0) : 
		return(True)
	else : 
		i += skip_useless(string,i)
		if(i == len(string)) : 
			return(True)
		else : 
			return(False)

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

			if(word_array[7] != []) : 
				print('others : ')
				for strings in word_array[7] : 
					print(strings)
				print()

			if(word_array[8] != '') : 
				print('category : ' + word_array[8])

	print('------------------------')