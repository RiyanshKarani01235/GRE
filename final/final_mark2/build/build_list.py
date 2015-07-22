from final_mark2.common import debug
from final_mark2.build.decode import decode_meaning_and_clue
from final_mark2.build.decode import search_list_others_to_add_other_words_to_list
from final_mark2.common.string_handling import *

working_directory = '/users/ironstein/desktop/final_mark2'

list_of_everything = []
number_of_words = 0

def build_word_list(w) : 

	#[word,figure_of_speech,meaning,clue,sentence,synonym,antonym,others,category]
	words = w
	global list_of_everything
	global number_of_words

	i = 0
	category = ''
	while(i < len(words)) :
		data = read(words,i)
		i += data[1]
		data = data[0]
		if(data[8] != []) : 
			category = data[8]
		data[8] = category
		list_of_everything.append(data)
		number_of_words += 1

	for word_array in list_of_everything : 
		for element in word_array : 
			if((element != []) and (type(element) != type(''))) : 
				for i in range(len(element)) :
					element[i] = caps_to_small(element[i])

	print('done building list')
	return(search_list_others_to_add_other_words_to_list(list_of_everything))

def read(words,i) : 
	
	global number_of_words
	global list_of_everything
	word = []
	figure_of_speech = []
	meaning = []
	clue = []
	sentence = []
	synonym = []
	antonym = []
	others = []
	category = []
	j = i
	j += skip_useless(words,j)

	if(char_to_int(words[j]) < 96) :
		#capital letter means category

		if(words[j] == '#') : 
			category = '#'
			j += 1
		else : 
			string = ''
			while(words[j] != '\n') : 
				string += words[j]
				j += 1
			j += 1
			category = caps_to_small(remove_useless(string))

	j += skip_useless(words,j)

	data = record_until_character(words,'(',j)
	word.append(data[0])
	j += data[1]
	j += 1

	if(category == '#') : 
		string = '-' + data[0]
		list_of_everything[number_of_words-1][7].append(string)

	data = record_until_character(words,')',j)
	figure_of_speech.append(data[0])
	j += data[1]
	j += 1
	
	j += skip_until_character(words,':',j)
	j += 1

	j += skip_useless(words,j)

	data = record_until_character(words,';',j)
	meaning = data[0]
	j += data[1]
	j += 1

	data = decode_meaning_and_clue(meaning)
	meaning = data[0]
	clue = data[1]

	if(j != len(words)) : 
		j += skip_useless(words,j)

	array = []
	while(j < len(words)) : 
		if(words[j] == '-') : 
			j += 1
			data = record_until_character(words,'\n',j)
			array.append(data[0])
			j += data[1]
			j += 1
		else :
			break
	for k in range(len(array)) : 
		first_word = get_word(array[k],1,'remove symbols')
		if((first_word == 'synonyms') or (first_word == 'synonym')) : 
			string = remove_word(remove_word((remove_word(array[k],':')),'synonyms'),'synonym')
			list_of_words = words_from_string(string)
			for word_ in list_of_words : 
				synonym.append(word_)
		elif((first_word == 'antonyms') or (first_word == 'antonym')): 
			string = remove_word(remove_word((remove_word(array[k],':')),'antonyms'),'antonym')
			antonym.append(string)
		elif((first_word == 'sentence') or (first_word == 'sentences')) : 
			string = remove_word(remove_word((remove_word(array[k],':')),'sentences'),'sentence')
			sentence.append(string)
		else : 
			others.append(array[k])
	return([[word,figure_of_speech,meaning,clue,sentence,synonym,antonym,others,category],j-i])
