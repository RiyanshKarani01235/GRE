from string_handling import *
import os
from debug import debug
from decode import decode_meaning_and_clue
from decode import search_list_others_to_add_other_words_to_list

working_directory = '/users/ironstein/documents/projects working directory/GRE/final/final_mark2'

def setup() :
	
	os.chdir(working_directory)
	words = open('words','r+')
	words_ = words.read()
	words.close()
	words = words_
	del(words_)
	return(words)

def run() : 

	#[word,figure_of_speech,meaning,clue,sentence,synonym,antonym,others,category]

	words = setup()
	list_of_everything = []
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
	print('done building list')
	return(search_list_others_to_add_other_words_to_list(list_of_everything))

def read(words,i) : 

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
		elif((first_word == 'antonyms') or (first_word == 'antonym')): 
			string = remove_word(remove_word((remove_word(array[k],':')),'antonyms'),'antonym')
		elif((first_word == 'sentence') or (first_word == 'sentences')) : 
			string = remove_word(remove_word((remove_word(array[k],':')),'sentences'),'sentence')
		else : 
			others.append(array[k])

	return([[word,figure_of_speech,meaning,clue,sentence,synonym,antonym,others,category],j-i])

def print_everything_about_word(array) : 
	print_array = ['word','figure_of_speech','meaning','clue','sentence','synonyms','antonyms','others','category']
	for i in range(9) : 
		string = print_array[i] + ' --> '
		print(string,array[i])
	print()

# l = run()
# for i in range(len(l)) : 
# 	print_everything_about_word(l[i])
