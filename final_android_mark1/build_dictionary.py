'''
builds a dictionary of words linking to other words
'''

from build_list import run
from string_handling import *

def build_word_dictionary(l) :

	dictionary = {}
	word_list = []
	for list_ in l : 
		word_list.append(list_[0][0])

	for word in word_list : 
		dictionary[word] = ()
	words_list = crawler(l)

	#---------------------------------
	# return_list = []
	# for list_ in words_list : 
	# 	_list_ = []
	# 	for word in list_ : 
	# 		if word not in word_list : 
	# 			_list_.append(word) 
	# 	return_list.append(_list_)
	#--------------------------------
	#print(words_list)
	# return_list = []
	# print('\n\n')
	# for i in range(len(words_list)) : 
	# 	list_ = []
	# 	print(words_list[i])
	# 	for word in words_list[i] : 
	# 		if(word != word_list[i]) : 
	# 			list_.append(word)
	# 	return_list.append(list_)
	# 	print(list_)
	# 	print('\n\n---------------------------')

	# print(return_list)

	# words_list = return_list
	# del(return_list)
	for i in range(len(words_list)) : 
		for word in words_list[i] : 
			if ((word in word_list) and (word != word_list[i])): 
				dictionary[word_list[i]] = append_to_tuple(dictionary[word_list[i]],word)

	print(dictionary)
	print('done building dictionary')
	return(dictionary)

word_list = []
def crawler(l) :
	'''
	returns a list of lists, each list consisting of words
	pertaining to the corresponding word, in the list, returned
	by the run() method of the build_list.py module 
	'''
	global word_list
	def crawler_(l) : 
		for i in l : 
			if(type(i) == list) : 
				crawler_(i)
			else : 
				word_list.append(i)

	word_list_ = []
	for i in range(len(l)) : 
		if(type(l[i]) == list) : 
			crawler_(l[i])
		word_list_.append(word_list)
		word_list = []

	return_word_list = []
	for i in range(len(word_list_)) : 
		return_word_list_ = []
		for j in range(len(word_list_[i])) : 
			words = words_from_string(word_list_[i][j])
			for k in range(len(words)) : 
				return_word_list_.append(words[k])
		return_word_list.append(return_word_list_)

	return_word_list_ = []
	for list_ in return_word_list : 
		words_ = []
		for i in range(2,len(list_)) : 
			words_.append(list_[i])
		return_word_list_.append(words_)

	print('done crawling')
	return(return_word_list_)

def append_to_tuple(tuple_,word) : 
	list_ = []
	for i in range(len(tuple_)) : 
		list_.append(tuple_[i])
	list_.append(word)
	return(tuple(list_))

build_word_dictionary(run())