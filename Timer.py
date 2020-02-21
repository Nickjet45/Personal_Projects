import time
import tkinter as tk
from tkinter import *

def destroy_screen():
    screen.destroy()


def set_Timer(set_hour, set_minute, set_second):

    while set_hour or set_minute or set_second > 0:
        if set_second == 0:
            set_minute = set_minute - 1
            set_second = 60
        if set_minute == 0 and set_hour is not 0:
            set_hour = set_hour - 1
            set_minute = 60
        if set_minute <= 0 and set_hour is not 0:
            set_hour = set_hour - 1
            set_minute = 60
        if set_minute == 0 and set_hour == 0 and set_second == 0:
            break
        set_second = set_second - 1
        print('{}h {}m {}s'.format(set_hour, set_minute, set_second))
        time.sleep(1)
    print("Timer is over")


def create_GUI():
    global desired_hours
    global desired_minutes
    global desired_seconds
    global screen

    screen = Tk()
    screen.geometry("300x300")
    screen.title("Timer GUI")

    desired_hours = IntVar()
    desired_minutes = IntVar()
    desired_seconds = IntVar()

    Label(text="Digital Timer").pack()
    Label(text="").pack()

    Label(text="Input number of Hours").pack()
    Hours = Entry(textvariable=desired_hours)
    Hours.pack()

    Label(text="").pack()
    Label(text="Input number of minutes").pack()
    Minutes = Entry(textvariable=desired_minutes)
    Minutes.pack()

    Label(text="").pack()
    Label(text="Input number of seconds").pack()
    Seconds = Entry(textvariable = desired_seconds)
    Seconds.pack()

    Label(text="").pack()
    Button(text="Begin Timer",width=20, height=2, command=run_Timer).pack()

    Label(text="").pack()
    Button(text="Close Application", command=destroy_screen, width=20, height=2).pack()

    screen.mainloop()


def run_Timer():
    desired_hour = desired_hours.get()
    desired_minute = desired_minutes.get()
    desired_second = desired_seconds.get()
    set_Timer(desired_hour, desired_minute, desired_second)


create_GUI()