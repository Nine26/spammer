import pyautogui
import time
from tkinter import *
import tkinter as tk


root = Tk()
root.title('spammer')


placeholder = 'enter the thing that you want to spam here'

def erase(event=None):
    if e.get() == placeholder:
        e.delete(0,'end')
def add(event=None):
    if e.get() == '':
        e.insert(0,placeholder)

e = Entry(root, width=50, borderwidth=3)
e.pack()

add()
e.bind('<FocusIn>',erase)
e.bind('<FocusOut>',add)





def spam():
    time.sleep(5)
    while True:
        pyautogui.typewrite(e.get())
        pyautogui.press("Enter")



myButton = Button(root, text="Start", command=spam)
myButton.pack()
quitButton = Button(root, text="Quit", command=root.quit)
quitButton.pack()


root.mainloop()

