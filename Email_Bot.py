import smtplib
from smtplib import SMTP
# Function to automatically send emails from a separate email
# Has 3 defined parameters



def Mail_Bot(email, subject_msg, body_msg):
    try:
        print('Connecting to server...')
        server: SMTP = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Logins to a predefined email address, must include the login token or password
        server.login('Email Username', 'Email secret password')

        # Defines the bulk of the email, including the subject and the body
        subject = subject_msg
        body = body_msg
        msg = f'subject: {subject}\n\n {body}'

        # Sends the email to whatever receiving_email is inputted
        server.sendmail('python3autobot@gmail.com',
                        email,
                        msg)

        print('Email has successfully been sent to: ' + email)

    except Exception as e:
        print(e)

    finally:
        # Logs out of the account
        server.quit()

