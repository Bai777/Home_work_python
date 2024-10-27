from tkinter import *

window = Tk()
window.title('Window input text')
window.geometry('400x400')

labelWindow = Label(text='Window input')
labelWindow.pack()

entryWindow = Entry()
entryWindow.pack()


window.mainloop()

