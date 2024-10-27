from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

window = Tk()
window.title('Напоминание')

labelRemin = Label(text='Установите напоминание')
labelRemin.pack(pady=10)

setButton = Button(text='Установить напоминание', command=setRemin)
setButton.pack()



window.mainloop()