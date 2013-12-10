
from random import choice
import smtplib
from email.mime.text import MIMEText


class TheWonderCouple:

    def __init__(self):
        self.gifter = -1
        self.gifted = -1
        self.email = ''

    def setGloriousSettings(self, gifter, gifted, email):
        self.gifter = gifter
        self.gifted = gifted
        self.email = email


class TheAwesomeCoupleMixer:

    def __init__(self):
        self.wonder_couples = []

    def magicMixer(self, emails):
        num_couples = len(emails)
        gifters = range(1, num_couples + 1)
        gifteds = range(1, num_couples + 1)
        for email in emails:
            gifter = gifted = choice(gifters)
            gifters.remove(gifter)
            while(gifter == gifted):
                gifted = choice(gifteds)
            gifteds.remove(gifted)
            twc = TheWonderCouple()
            twc.setGloriousSettings(gifter, gifted, email)
            self.wonder_couples.append(twc)

    def getWonderCouples(self):
        return self.wonder_couples


class TheFabulousMailer:

    def __init__(self, smtp_server, smtp_port, from_email, from_email_pwd, subject):
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
            print "Sending to ", wonder_couple.email
            to_email = wonder_couple.email
            msg_text = """
                Sois o casal %s
                Ides ofertar presentes ao casal %s

                'mai nada!

                """ % (wonder_couple.gifter, wonder_couple.gifted)
            message = MIMEText(msg_text)
            message['From'] = self.from_email
            message['To'] = to_email
            message['Subject'] = self.subject
            server.sendmail(self.from_email, to_email, message.as_string())
        server.quit()
        print "All done!"


##  couples settings
casais = []

##  smtp server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587

from_email = ''
from_email_pwd = ""
subject = 'A roleta do jantar de Natal do sexta rodou!!'

## run the thing
tacm = TheAwesomeCoupleMixer()
tacm.magicMixer(casais)
wonder_couples = tacm.getWonderCouples()

tfm = TheFabulousMailer(smtp_server, smtp_port, from_email, from_email_pwd, subject)
tfm.performLegendarySending(wonder_couples)
