'''
SMTP module
email.message
--> generated pass :-fvvr ynph wfnj hgno

code:-
import smtplib
import ssl
from email.message import EmailMessage
sender_email = "abc@gmail.com"
password = "fvvrynphwfnjhgno"

receiver_email = "import smtplib
import ssl
from email.message import EmailMessage
sender_email = "abc@gmail.com"
password = "fvvrynphwfnjhgno"

receiver_email = "xyz@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Hi Pari!"
message.set_content(f'''
                    Hello Parimala!

                    Welcome to our  Python class

                    Regards,
                    Python Team...''')

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
    
-------------------------------------------
#code for multipule users

import smtplib
import ssl
from email.message import EmailMessage
sender_email = "radha19962005@gmail.com"
password = "fvvrynphwfnjhgno"

receiver_email = "jahnavisaidevi@gmail.com","radhanstl19@gmail.com","parimalapathivada@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Hi Pari!"
message.set_content(f'''
                    Hello Radha!

                    Welcome to our  Python class

                    Regards,
                    Python Team...''')

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
    
    
'''

import smtplib
import ssl
from email.message import EmailMessage
sender_email = "radha19962005@gmail.com"
password = "fvvrynphwfnjhgno"

receiver_email = "jahnavisaidevi@gmail.com","radhanstl19@gmail.com","parimalapathivada@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Hi Pari!"
message.set_content(f'''
                    Hello Parimala!

                    Welcome to our  Python class

                    Regards,
                    Python Team...''')

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
    
