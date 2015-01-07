
from random import choice
import smtplib
from email.mime.text import MIMEText
import random


class TheWonderCouple:

    def __init__(self):
        self.gifter_email = ''
        self.gifted_email = ''

    def setGloriousSettings(self, gifter_email, gifted_email):
        self.gifter_email = gifter_email
        self.gifted_email = gifted_email


class TheAwesomeCoupleMixer:

    def __init__(self):
        self.wonder_couples = []

    def magicMixer(self, emails):
        num_couples = len(emails)
        gifters = range(num_couples)
        gifteds = range(num_couples)
        for email in emails:
            gifter = gifted = choice(gifters)
            gifters.remove(gifter)
            while(gifter == gifted):
                gifted = choice(gifteds)
            gifteds.remove(gifted)
            twc = TheWonderCouple()
            gifter_email = emails[gifter]
            gifted_email = emails[gifted]
            twc.setGloriousSettings(gifter_email, gifted_email)
            self.wonder_couples.append(twc)

    def getWonderCouples(self):
        return self.wonder_couples


class TheFabulousMailer:

    def __init__(self, smtp_server, smtp_port, from_email, from_email_pwd, subject, price):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.from_email_pwd = from_email_pwd
        self.subject = subject

    def performLegendarySending(self, wonder_couples):
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.from_email, self.from_email_pwd)
        for wonder_couple in wonder_couples:
            print "Sending to ", wonder_couple.gifter_email
            to_email = wonder_couple.gifter_email
            msg_text = """
                Sois o casal %s
                Ides ofertar presentes ao casal %s
                um presente com valor inferior a: %s (euros)

                'mai nada!

                """ % (wonder_couple.gifter_email, wonder_couple.gifted_email, price)
            message = MIMEText(msg_text)
            message['From'] = self.from_email
            message['To'] = to_email
            message['Subject'] = self.subject
            server.sendmail(self.from_email, to_email, message.as_string())
        server.quit()
        print "All done!"


##  price settings
max_price = 10

##  couples settings
casais = []

##  smtp server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587

from_email = ''
from_email_pwd = ""
subject = 'A roleta do jantar de Natal do sexta rodou e deciciu!!'

## run the thing
tacm = TheAwesomeCoupleMixer()
tacm.magicMixer(casais)
wonder_couples = tacm.getWonderCouples()
price = round(random.random() * max_price, 2)

tfm = TheFabulousMailer(smtp_server, smtp_port, from_email, from_email_pwd, subject, price)
tfm.performLegendarySending(wonder_couples)
