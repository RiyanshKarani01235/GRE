# class dictionary :

#     def __init__(self) :
#         self.l = run()
#         self.r = read_functions()

#     def meaning(self,word) :
#         if(self.in_list(word)[0]) :
#             i = self.in_list(word)[1]
#             print(self.l[2][i])
#             print(self.l[3][i])
#         else :
#             print('not available')

#     def in_list(self,word) :
#         for i in range(len(self.l[0])) :
#             if(self.l[0][i] == word) :
#                 return [True,i]
#         return [False]

#     def edit_word(self,word) :
#         string = ''
#         for i in range(len(word)) :
#             if(word[i] != ' ') :
#                 string += word[i]
#         return self.r.caps_to_small(string)
    
#     def dictionary(self) :
#         while(1) :
#             word = self.edit_word(input('enter a word : '))
#             if(word == 'exit') :
#                 break
#             else :
#                 self.meaning(word)
#                 print('\n')

# class test :

#     def __init__(self) :
#         self.l = run()
#         self.r = read_functions()
#         self.r_ = run_functions()
#         self.most_common_words = []
#         m = open('most_common_words','r')
#         for line in m:
#             self.most_common_words.append(self.r.caps_to_small(self.remove_newline(line)))
#         m.close()

#     def remove_newline(self,word) :
#         return_word = ''
#         for i in range(len(word)) :
#             if(word[i] != '\n') :
#                 return_word += word[i]
#         return return_word
    
#     def in_between(self,n,a,b) :
#         if((n >= a) and (n <= b)) :
#             return True
#         return False
    
#     def words_from_sentence(self,sentence) :
#         word_list = []
#         return_list = []
#         i = 0
#         while(i < len(sentence)) :
#             word = ''
#             while((i < len(sentence)) and (self.in_between(self.r.char_to_int(sentence[i]),65,90) or self.in_between(self.r.char_to_int(sentence[i]),97,122))) :
#                 word += sentence[i]
#                 i += 1
#             word_list.append(word)
#             i += 1
#         for i in range(len(word_list)) :
#             if(word_list[i] != '') :
#                 return_list.append(word_list[i])
#         return return_list

#     def in_list(self,l,word) :
#         for i in range(len(l)) :
#             if (l[i] == word) :
#                 return True
#         return False

#     def remove_common_words(self,l) :
#         l_ = []
#         for i in range(len(l)) :
#             if(not(self.in_list(self.most_common_words,l[i]))) :
#                 l_.append(l[i])
#         return l_
                
#     def match(self,a,b) :
#         a_ = self.remove_common_words(a)
#         b_ = self.remove_common_words(b)

#         count = 0
#         for i in range(len(a_)) :
#             if(self.in_list(b_,a_[i])) :
#                 count += 1

#         c = count*1.0/len(a_)

#         if(c == 0) :
#             return 'NOT AT ALL'
#         if(c < 0.25) :
#             return 'MILDLY TRUE'
#         if(c < 0.5) :
#             return 'HALFWAY THERE'
#         if(c < 0.75) :
#             return 'CLOSE'
#         if(c < 1) :
#             return 'ALMOST'
#         return 'PERFECT'
        
    
#     def check_if_true(self,answer,i) :
#         expected_answer_array = self.words_from_sentence(self.l[2][i])
#         answer_array = self.words_from_sentence(answer)
        
#         for i in range(len(expected_answer_array)) :
#             expected_answer_array[i] = self.r.caps_to_small(expected_answer_array[i])
#         for i in range(len(answer_array)) :
#             answer_array[i] = self.r.caps_to_small(answer_array[i])
            
#         return(self.match(expected_answer_array,answer_array))

#     def print_everything(self,i) :
#         print('word --> ' + self.l[0][i] + '(' + self.l[1][i] + ')')
#         if(self.l[7][i] != 'not available') :
#             print('category --> ' + self.l[7][i]) 
#         print('meainng --> ' + self.l[2][i])
#         if(self.l[4][i] != 'not available') :
#             string = ''
#             for j in range(len(self.l[4][i])) :
#                 string += self.l[4][i][j]
#                 string += ' '
#             print ('synonyms --> ' + string)
#         if(self.l[5][i] != 'not available') :
#             string = ''
#             for j in range(len(self.l[5][i])) :
#                 string += self.l[5][i][j]
#                 string += ' '
#             print ('synonyms --> ' + string)
#         if(self.l[8][i] != 'not available') :
#             for j in range(len(self.l[8][i])) :
#                 print(self.l[8][i][j])
    
#     def test(self) :

#         while(1) :
#             i = random.randint(0,len(self.l[0])-1)
#             word = self.l[0][i]
#             print('guess the meaning of the word --> ' +word)
#             answer = input('do you want a clue ? ')
#             if(answer == 'yes') :
#                 print(self.l[3][i])
#                 answer = input('now do you have a clue ???     ')
#                 if(self.check_if_true(answer,i)) :
#                     print('PERFECT')
#                     print()
#                     self.print_everything(i)
#                     log = 0.5

#                 else :
#                     self.print_everything(i)
#                     log = 0
#             elif(answer == 'exit') :
#                 break
#             else :
#                 response = self.check_if_true(answer,i)
#                 print(response)
#                 if(response != 'PERFECT') :
#                     print('heres a clue for you. Try again please ')
#                     print(self.l[3][i])
#                     answer = input('guess the meaning : ')
#                     response = self.check_if_true(answer,i)
#                     print()
#                     self.print_everything(i)
#                 else :
#                        log = 1
#             print ('---------------------------------------------')

                

# #--------------------------------------------------------------------

# def dictionary_mode() :
#     d = dictionary()
#     d.dictionary()

# def test_mode() :
#     t = test()
#     t.test()

from build_list import run

def main() : 
	function_name = input('what do you want to do ? ')
	if(function_name == 'dictionary') : 
		dictionary()
	else : 
		print('sorry, no such function available')
		main()

def dictionary() :
        list_of_everything = run()
        word_list = []
        for i in range(len(list_of_everything)) :
                word_list.append(list_of_everything[i][0][0])
        print(word_list)
        while(1) : 
                word = input('enter a word : ')
                if(word in word_list) :
                        print('exists')
                elif(word == 'exit') :
                        print('exiting')
                        print('-----------------------------------')
                        print()
                        main()
                else :
                        print('word not available')

main()
