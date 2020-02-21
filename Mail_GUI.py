import smtplib
import tkinter as tk
from tkinter import *
import sqlite3


def Send_Email():
    receiver = recipient.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('python3autobot@gmail.com', 'aqhqyaghpowicxxt')

    subject = email_subject.get()
    body = email_body.get()

    msg = f'subject: {subject} \n\n {body}'

    server.sendmail('python3autobot@gmail.com',
                    receiver,
                    msg)
    print("Email successfully sent to: " + receiver)
    server.quit()

    screen.destroy()


def Input_Information():
    global screen
    global email_body
    global email_subject
    global recipient

    screen = Tk()
    screen.geometry("500x400")
    screen.title('Email')

    Label(text="").pack()
    Label(text="Email Recipient").pack()

    recipient = StringVar()
    email_subject = StringVar()
    email_body = StringVar()

    recipient = Entry(textvariable=recipient)
    recipient.pack()
    Label(text="").pack()

    Label(text="Subject of Email").pack()
    email_subject = tk.Entry(textvariable=email_subject)
    email_subject.pack()
    Label(text="").pack()

    Label(text="Body of Email").pack()
    email_body = tk.Entry(textvariable=email_body)
    email_body.pack()
    Label(text="").pack()

    Button(text="Send email", command=Send_Email, width=40, height=3, bg="black", fg="green").pack(side="bottom",
                                                                                                   ipadx=10, ipady=10)

    screen.mainloop()


Input_Information()
