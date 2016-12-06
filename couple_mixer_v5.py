
from random import choice, uniform
import smtplib
import requests
from email.mime.text import MIMEText


class TheWonderCouple:

    def __init__(self, gifter_email, gifted_email, joke):
        self.gifter_email = gifter_email
        self.gifted_email = gifted_email
        self.joke = joke


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
            joke = CoJoTheEntertainer.getHilariousParticipation()
            twc = TheWonderCouple(emails[gifter], emails[gifted], joke)
            self.wonder_couples.append(twc)

    def getWonderCouples(self, emails):
        self.magicMixer(emails)
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
                Sois o casal {gifter_email}
                Ides ofertar presentes ao casal {gifted_email}
                um presente com valor igual ou inferior a: {price}

                And I say to you: {joke}

                'mai nada!

                """.format(gifter_email=wonder_couple.gifter_email,
                           gifted_email=wonder_couple.gifted_email,
                           price=price,
                           joke=wonder_couple.joke)
            message = MIMEText(msg_text)
            message['From'] = self.from_email
            message['To'] = to_email
            message['Subject'] = self.subject
            server.sendmail(self.from_email, to_email, message.as_string())
        server.quit()
        print "All done!"


class TheIntrepidPriceFinder:

    def __init__(self, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price

    def getThePriceForHappiness(self):
        price = round(uniform(self.min_price, self.max_price), 2)
        return str(price)


class CoJoTheEntertainer:

    @staticmethod
    def getHilariousParticipation():
        r = requests.get('http://api.icndb.com/jokes/random')
        if r.status_code == 200:
            the_line = r.json()
            return the_line['value']['joke']
        else:
            return "No joke for you"





##  price settings
min_price = 11
max_price = 20

##  couples settings
couples = []

##  smtp server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587

from_email = ''
from_email_pwd = ""
subject = 'A roleta do jantar de Natal do sexta rodou e deciciu!!'

## run the thing
tacm = TheAwesomeCoupleMixer()
wonder_couples = tacm.getWonderCouples(couples)
tipf = TheIntrepidPriceFinder(min_price, max_price)
price = tipf.getThePriceForHappiness()

tfm = TheFabulousMailer(smtp_server, smtp_port, from_email, from_email_pwd, subject, price)
tfm.performLegendarySending(wonder_couples)
