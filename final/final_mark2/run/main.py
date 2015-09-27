import pkg_resources
import __init__
working_directory = '/Users/ironstein/Documents/projects working directory/GRE/GRE codes/GRE final/final/'
__init__.__init__(working_directory)
import os

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
	
	FLAG = 0
	
	w = ''

	word_lists = []

	if FLAG is 0 :

		word_lists = ['common words 1', 'common words 2', 'common words 3', 'common words 4','common words 5','common words 6','random words',\
		'basic words 1','basic words 2','basic words 3','basic words 4','basic words 5','basic words 6']
		# include_words_list = [0,0,0,0,0,0,0,0,0,0,0,1,0]
		# include_words_list = [1,1,1,1,1,1,0,0,0,0,0,0,0] #common words all
		# include_words_list = [1,0,1,0,1,0,0,0,0,0,0,0,0] #common words 1,3,5
		# include_words_list = [0,1,0,1,0,1,0,0,0,0,0,0,0] #common words 2,4,6
		# include_words_list = [0,0,0,0,0,0,0,1,1,1,0,0,0] #basic words 1,2,3
		# include_words_xlist = [1,1,1,1,1,1,0,1,1,1,1,1,1] #all

		for word_list in word_lists :
			if include_words_list[word_lists.index(word_list)] is 1 :
				print(word_list)
				# print(w)
				words = pkg_resources.resource_filename('final_mark2.words',word_list)
				words = open(words,'r+')
				words_ = words.read()
				words.close()
				del(words)
				w += (words_)
		# for line in w : 
		# 	print(line)
		# print(w)

		input_ = input('do you want just the list of everything ? y/n ')
		if input_ is 'y' : 
			path = 'final_mark2.words'
			for word_list in word_lists :
				if include_words_list[word_lists.index(word_list)] is 1 : 
					print('\n')
					print('----------------------------',end=' ')
					print(word_list,end=' ')
					print('----------------------------',end='\n\n')
					words = pkg_resources.resource_filename(path,word_list)
					words = open(words,'r+')
					words_ = words.read()
					words.close()
					del(words)
					print(words_)
			while(1) : 
				pass

	
	else : 
		os.chdir(working_directory + 'final_mark2/words/category wise words/')
		l = os.listdir()

		ALL = 0

		flags = [

			[0,'Abbrevated communication'],\
			[0,'Act quickly'],\
			[0,'Assist'],\
			[0,'Bad mood'],\
			[0,'Beginner_Amateur'],\
			[0,'Beginner_Young'],\
			[0,'Biting(as in wit or temperament)'],\
			[0,'Bold'],\
			[0,'Boring'],\
			[0,'Carousal'],\
			[0,'Changing quickly'],\
			[0,'Copy'],\
			[0,'Criticize_Criticism'],\
			[0,'Death_Mourning'],\
			[0,'Denying of self'],\
			[0,'Dictatorial'],\
			[0,'Difficult to understand'],\
			[0,'Disgusting_Offensive'],\
			[0,'Easy to understand'],\
			[0,'Eccentric_Dissimilar'],\
			[0,'Embarass'],\
			[0,'Equal'],\
			[0,'Falsehood'],\
			[0,'Family'],\
			[0,'Favouring_Not impartial'],\
			[0,'Forgive'],\
			[0,'Funny'],\
			[0,'Gaps_Openings'],\
			[0,'Generous_Kind'],\
			[0,'Greedy'],\
			[0,'Hardhearted'],\
			[0,'Harmful'],\
			[0,'Harsh-sounding'],\
			[0,'Hatred'],\
			[0,'Healthy'],\
			[0,'Hesitate'],\
			[0,'Hostile'],\
			[0,'Innocent_Inexperienced'],\
			[0,'Insincere'],\
			[0,'Investigate'],\
			[0,'Lazy_Sluggish'],\
			[0,'Luck'],\
			[0,'Nag'],\
			[0,'Nasty'],\
			[0,'Not a straight line'],\
			[0,'Overblown_Wordy'],\
			[0,'Pacify_Satisfy'],\
			[0,'Plesant_Sounding'],\
			[0,'Poor'],\
			[0,'Praise'],\
			[0,'Predict'],\
			[0,'Prevent_Obstruct'],\
			[0,'Smart_Learned'],\
			[0,'Sorrow'],\
			[0,'Stubborn'],\
			[0,'Terse'],\
			[0,'Time_Order_Duration'],\
			[0,'Timid_Timidity'],\
			[0,'Truth'],\
			[0,'Unusual'],\
			[0,'Walking about'],\
			[0,'Wandering'],\
			[0,'Weaken'],\
			[0,'Wisdom'],\
			[0,'Withdrawal_Retreat'],\

		]

		if ALL is 0 :
			for element in flags : 
				if element[0] is 1 : 
					word_lists.append(element[1])
		else : 
			for element in flags : 
				word_lists.append(element[1])

		print(len(l))

		for word_list in word_lists :
			if ALL is 0 :
				print(word_list)
			# print(w)
			words = pkg_resources.resource_filename('final_mark2.words.category wise words',word_list)
			#print(words)
			words = open(words,'r+')
			words_ = words.read()
			words.close()
			del(words)
			w += (words_)

		input_ = input('do you want just the list of everything ? y/n ')
		if input_ is 'y' : 
			path = 'final_mark2.words.category wise words'
			for word_list in flags :
				if (word_list[0] is 1) or (ALL is 1) : 
					print('\n')
					print('----------------------------',end=' ')
					print(word_list[1],end=' ')
					print('----------------------------',end='\n\n')
					words = pkg_resources.resource_filename(path,word_list[1])
					words = open(words,'r+')
					words_ = words.read()
					words.close()
					del(words)
					print(words_)
			while(1) : 
				pass

		os.chdir(working_directory)
	
	return w

def main() :

	global LIST
	global DICTIONARY
	words = setup()
	LIST = build_word_list(words)
	print(len(LIST))
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
