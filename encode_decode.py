from tkinter import *
import base64

#initialize the window
root = Tk()
root.geometry('500x300')
root.resizable(0,0) #(0,0) won't allow to window to resize
root.title('Message Encode and Decode')

Label(root, text = 'ENCODE DECODE', font = 'arial 20 bold').pack()

#define variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

############define function############
def encode(key, message):
	pass

def Decode(key, message):
	pass

def Mode():
	pass

def Exit():
	pass

def Reset():
	pass

##########other widgets##########
#Message
Label(root, font = 'arial 12 bold', text = 'MESSAGE').place(x = 60, y = 60) #label.place() allows to have more accurate postioning than pack() or grid(). Also allows to allow one above another or vice versa.
Entry(root, font = 'arial 10', textvariable = Text, bg =  'ghost white').place(x = 290, y = 60)

#key
Label(root, font = 'arial 12 bold', text = 'KEY').place(x = 60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key, bg = 'ghost white').place(x = 290, y = 90)

#mode
Label(root, font = 'arial 12 bold', text = 'MODE(e-encode, d-decode)').place(x = 60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode, bg = 'ghost white').place(x = 290, y = 120)

#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg = 'ghost white').place(x = 290, y = 150)

#result button
Button(root, font = 'arial 10 bold', text = 'RESULT', padx = 2, bg = 'LightGray', command = Mode).place(x = 60, y = 150)

#reset button
Button(root, font = 'arial 10 bold', text = 'RESET', width = 6, command = Reset, bg = 'LimeGreen', padx = 2).place(x = 80, y = 190)

#exit button
Button(root, font = 'arial 10 bold', text = 'EXIT', width = 6, command = Exit, bg = 'OrangeRed', padx = 2, pady =2).place(x =180, y = 190)

root.mainloop()
