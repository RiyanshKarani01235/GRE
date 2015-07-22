'''
builds a dictionary of words linking to other words
'''

from final_mark2.common.string_handling import *
old_dictionary = {}

def build_word_dictionary(_list_) :

	l = _list_
	dictionary = {}
	word_list = []
	for list_ in l : 
		word_list.append(list_[0][0])

	for word in word_list : 
		dictionary[word] = ()
	words_list = crawler(l)

	for i in range(len(words_list)) : 
		for word in words_list[i] : 
			if ((word in word_list) and (word != word_list[i]) and (word not in dictionary[word_list[i]])): 
				dictionary[word_list[i]] = append_to_tuple(dictionary[word_list[i]],word)

	for word in word_list : 
		for word_ in dictionary[word] : 
			if(word not in dictionary[word_]) : 
				dictionary[word_] = append_to_tuple(dictionary[word_],word)

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

