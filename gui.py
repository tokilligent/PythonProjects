from tkinter import *
from PIL import ImageTk,Image
from pynput.keyboard import Listener

root = Tk()

root.title('GUI for Arduino')

def forward():
    label = Label(root,text="You pressed Up")
    label.grid(row = 3, column = 0)

def left():
    label = Label(root,text="You pressed Left")
    label.grid(row = 3, column = 0)

def right():
    label = Label(root,text="You pressed Right")
    label.grid(row = 3, column = 0)

def backward():
    label = Label(root,text="You pressed Down")
    label.grid(row = 3, column = 0)

def stop():
    label = Label(root,text="You pressed Stop")
    label.grid(row = 3, column = 0)

def on_press(key):
    if(key.char=='w'):
        forward()
    elif(key.char=='a'):
        left()
    elif(key.char=='s'):
        backward()
    elif(key.char=='d'):
        right()

def on_release(key):
    stop()


button_1 = Button(root, text="Up",padx=40,pady=40, command=forward)
button_1.grid(row=0, column=1)

button_2 = Button(root, text="Left",padx=40,pady=40, command=left)
button_2.grid(row=1, column=0)

button_5 = Button(root, text="Stop",padx=40,pady=40, command=stop)
button_5.grid(row=1, column=1)

button_3 = Button(root, text="Right",padx=40,pady=40, command=right)
button_3.grid(row=1, column=2)

button_4 = Button(root, text="Down",padx=40,pady=40, command=backward)
button_4.grid(row=2, column=1)




with Listener(on_press=on_press, on_release=on_release) as listener:
    root.mainloop()

