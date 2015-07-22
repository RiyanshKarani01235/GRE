from build_list import run

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

def print_everything_about_word