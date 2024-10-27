from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

time_convert = None
stop_flag = False

def set_reminder():
    global time_convert, reminder_text
    reminder = sd.askstring('Введите время напоминания',
                            'Введите время напоминания '
                            'в формате ЧЧ:ММ в 24 часовом формате')
    if reminder:
        try:
            hour_remi = int(reminder.split(':')[0])
            minute_remi = int(reminder.split(':')[1])
            now_time = datetime.datetime.now()
            print(now_time)
            date_time = now_time.replace(hour=hour_remi,
                                         minute=minute_remi,
                                         second=0)
            print(date_time)
            time_convert = date_time.timestamp()
            print(time_convert)
            reminder_text = sd.askstring("Текст напоминания",
                                         "Введите текст напоминания:")
            labelRemin.config(text=f"Напоминание установлено на "
                                   f"{hour_remi:02}: {minute_remi:02}")
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка {e}')


def check_reminder():
    global time_convert
    if time_convert:
        now_time = time.time()
        if now_time >= time_convert:
            play_snd()
            time_convert = None
    window.after(10000, check_reminder)


def play_snd():
    global stop_flag
    stop_flag = True
    pygame.mixer.init()
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()

def stop_music():
    global stop_flag
    if stop_flag:
        pygame.mixer.music.stop()
        stop_flag = False
    labelRemin.config(text='Установить новое напоминание')

window = Tk()
window.title('Напоминание')
window.geometry('400x400')

labelRemin = Label(text='Установите напоминание', font=('Arial', 14))
labelRemin.pack(pady=10)

setButton = Button(text='Установить напоминание', command=set_reminder)
setButton.pack(pady=10)

stopButton = Button(text='Остановить музыку', command=stop_music)
stopButton.pack(pady=10)

check_reminder()

window.mainloop()