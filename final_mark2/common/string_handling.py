def char_to_int(c) : 
	for i in range(256) :
		if(chr(i) == c) : 
			return i
	print(c)

def skip_character(string,character,i) : 
	j = i
	while((j<len(string)) and (string[j] == character)) : 
		j += 1 

	return j-i

def skip_until_character(string,character,i) : 
	j = i
	while((string[j] != character)and(i<len(string))) : 
		j += 1

	return j-i

def record_until_character(string,character,i) : 
	j = i
	string_ = ''
	while((string[j] != character)and(i<len(string))) : 
		string_ += string[j]
		j += 1
	return [string_,j-i]


skip_useless_array = [' ','\n','\t']
def skip_useless(string,i) : 
	j = i
	while(string[j] in skip_useless_array) : 
		for k in range(len(skip_useless_array)) :
			j += skip_character(string,skip_useless_array[k],j)
		if(j >= len(string)) : 
			break
	return j-i

remove_useless_array = ['\n','\t']
def remove_useless(string) : 
	i = 0
	return_string = ''
	while(i < len(string)) : 
		if(not(string[i] in remove_useless_array)) : 
			return_string += string[i]
		i += 1 
	return(return_string)

def caps_to_small(string) :
        return_string = ''
        for i in range(len(string)) :
            if((char_to_int(string[i]) < 65) or (char_to_int(string[i]) > 90)) :
                return_string += string[i]
            else :
                return_string += chr(char_to_int(string[i]) + 32)
        return return_string

def is_alphabet(character) :
    i = char_to_int(character)
    if(((i>64) and (i<91)) or ((i>96) and (i<123))) :
        return True
    return False

def is_number(character) : 
	i = char_to_int(character) 
	if((i>47) and (i<58)) : 
		return True
	return False

def get_word(string,n,category) :
    array = []
    i = 0
    if(category == 'remove symbols') :
        while(i<len(string)) :
            string_ = ''
            while((not(is_alphabet(string[i]))) and (not(is_number(string[i])))):
                i += 1
                if(i>= len(string)) :
                    break
            if(i>= len(string)) :
                    break
            while((is_alphabet(string[i])) or (is_number(string[i]))) :
                string_ += string[i]
                i += 1
                if(i>= len(string)) :
                    break
            array.append(string_)
            if(i>= len(string)) :
                    break
        if(n > len(array)) :
            return None
        else :  
            return array[n-1]
    if(category == 'keep symbols') :
        while(i<len(string)) :
            string_ = ''
            while(string[i] == ' ') :
                i += 1
                if(i>= len(string)) :
                    break
            if(i>= len(string)) :
                    break
            while(not(string[i] == ' ')) :
                string_ += string[i]
                i += 1
                if(i>= len(string)) :
                    break
            array.append(string_)
            if(i>= len(string)) :
                    break
        if(n > len(array)) :
            return None
        else :  
            return array[n-1]

def remove_word(string,word) : 

	word_array = []
	i = 1
	while(1) : 
		word_ = get_word(string,i,'keep symbols')
		if(word_ == None) : 
			break
		else : 
			word_array.append(word_)
			i += 1

	# word_array = []

	# word_array.append(get_word(string,5,'keep symbols'))
	# print(word_array)
	string = ''
	for i in range(len(word_array)) : 
		if(not(word_array[i] == word)) : 
			string += word_array[i]
			string += ' '
	return(string)

def words_from_string(string) : 
	i = 1
	word_array = []
	while(1) : 
		word = get_word(string,i,'remove symbols')
		if(word == None) : 
			break
		else : 
			word_array.append(word)
			i += 1
	return word_array
