from tkinter import *
import time

root = Tk()

label1 = Label(root,text='name')
label2 = Label(root,text='password')
entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

def generate_color(red,green,blue) : 
	
	def decimal_to_hex_string(number) :

		def number_to_string(number) : 
			if(number < 10)  :
				return(str(number))
			else : 
				return(chr(97 + number - 10))

		num0 = int(number%16)
		num1 = int((number/16)%16)
		num2 = int(number/256)

		string = number_to_string(num2) + number_to_string(num1) + number_to_string(num0)
		return(string)

	if((red > 4095) or(green > 4095) or (blue > 4095)): 
		print('color value should be greater than 4095')
	else : 
		return('#' + decimal_to_hex_string(red) + decimal_to_hex_string(green) + decimal_to_hex_string(blue))

def handler(event) : 
	print('button pressed')


color = generate_color(2000,2000,2000)
button = Button(root,text='keep me logged in',bg=color)
button.bind('<Control-Motion>',handler)
button.grid(columnspan=2)




root.mainloop() 
