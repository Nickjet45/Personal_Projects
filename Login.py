import os
import tkinter as tk
from tkinter import *


def delete3():
    screen3.destroy()


def delete4():
    screen4.destroy()


def delete5():
    screen5.destroy()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration successful", fg="green", bg="black").pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username").pack()
    username_entry = tk.Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry = tk.Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Finish Registration", width=20,
           height=2, command=register_user).pack()


def login():
    global screen2
    global username_verify
    global password_verify
    global username_entered
    global password_entered

    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Please enter Login details").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="username").pack()
    username_entered = tk.Entry(screen2, textvariable=username_verify)
    username_entered.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password").pack()
    password_entered = tk.Entry(screen2, textvariable=password_verify)
    password_entered.pack()

    Button(screen2, text="Login", width=20,
           height=2, command=login_verify).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entered.delete(0, END)
    password_entered.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()


def login_success():
    screen2.destroy()
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")

    Label(screen3, text="Login successful").pack()
    Button(screen3, text="Ok", command=delete3).pack()


def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")

    Label(screen4, text="Incorrect password").pack()
    Button(screen4, text="Ok", command=delete4).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")

    Label(screen5, text="User not found").pack()
    Button(screen5, text="Ok", command=delete5).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x400")
    screen.title("Email Login")

    header = tk.Label(text="Login/Register Below", bg="grey", fg="black",
                      height="2", width="100", font=("Times", 13)).pack()

    Label(text="").pack()
    start_login = tk.Button(text="Login", bg="white", fg="black",
                            height="2", width="20", command=login).pack()
    start_register = tk.Button(text="Register", bg="white", fg="black",
                               height="2", width="20", command=register).pack()

    screen.mainloop()


main_screen()
