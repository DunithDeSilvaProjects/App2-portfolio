import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()
username = "dunithdesilva21@gmail.com"
password = ""
receiver="somethign@gmail.com"
message = """\
Subject: Hi!
How are you?
Bye!

"""
with smtplib.SMTP_SSL(host=host,port=port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)