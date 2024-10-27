from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

time_convert = 0


def set_reminder():
    global time_convert
    reminder = sd.askstring('Введите время напоминания',
                            'Введите время напоминания '
                            'в формате ЧЧ:ММ в 24 часовом формате')
    if reminder:
        try:
            hour_remi = int(reminder.split(':')[0])
            minute_remi = int(reminder.split(':')[1])
            now_time = datetime.datetime.now()
            print(now_time)
            date_time = now_time.replace(hour=hour_remi, minute=minute_remi)
            print(date_time)
            time_convert = date_time.timestamp()
            print(time_convert)
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка {e}')


def check_reminder():
    global time_convert
    if time_convert:
        now_time = time.time()
        if now_time >= time_convert:
            play_snd()
            time_convert = 0
    window.after(10000, check_reminder)


def play_snd():
    pygame.mixer.init()
    pygame.mixer_music.load('reminder.mp3')
    pygame.mixer.music.play()


window = Tk()
window.title('Напоминание')

labelRemin = Label(text='Установите напоминание')
labelRemin.pack(pady=10)

setButton = Button(text='Установить напоминание', command=set_reminder)
setButton.pack()



window.mainloop()