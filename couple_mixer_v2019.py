#!usr/bin/python
# -*- coding: utf-8 -*-
#

from random import choice, uniform
import smtplib
import requests
from email.mime.text import MIMEText
from datetime import date, timedelta
import getpass
import settings as s


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
        gifters = list(range(num_couples))
        gifteds = list(range(num_couples))
        for email in emails:
            gifter = gifted = choice(gifters)
            gifters.remove(gifter)
            while (gifter == gifted):
                gifted = choice(gifteds)
            gifteds.remove(gifted)
            joke = CoJoTheEntertainer.getHilariousParticipation()
            twc = TheWonderCouple(emails[gifter], emails[gifted], joke)
            self.wonder_couples.append(twc)

    def getWonderCouples(self, emails):
        self.magicMixer(emails)
        return self.wonder_couples


class TheFabulousMailer:
    def __init__(self, smtp_server, smtp_port, from_email, from_email_pwd, subject, price, inflation_rate):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.from_email_pwd = from_email_pwd
        self.subject = subject
        self.price = price
        self.inflation_rate = inflation_rate

    def performLegendarySending(self, wonder_couples):
        # server = smtplib.SMTP_SSL(self.smtp_server, 465)#self.smtp_port)
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.ehlo()
        #server.starttls()
        server.ehlo()
        server.login(self.from_email, self.from_email_pwd)
        for wonder_couple in wonder_couples:
            print("Sending to {gifter_email}".format(gifter_email=wonder_couple.gifter_email))
            to_email = wonder_couple.gifter_email
            msg_text = """
                Sois o casal {gifter_email}
                Ides ofertar presentes ao casal {gifted_email}
                um presente com valor exatamente igual a: {price}

                And I say to you: {joke}

                'mai nada!

                """.format(gifter_email=wonder_couple.gifter_email,
                           gifted_email=wonder_couple.gifted_email,
                           price=CoJoTheCapitalist.getCapitalistPrice(self.price, self.inflation_rate),
                           joke=wonder_couple.joke)
            message = MIMEText(msg_text)
            message['From'] = self.from_email
            message['To'] = to_email
            message['Subject'] = self.subject
            server.sendmail(self.from_email, to_email, message.as_string())
        server.quit()
        print("All done!")


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


class CoJoTheCapitalist:
    @staticmethod
    def getCapitalistPrice(price, inflation_rate):
        rate_date = CoJoTheCapitalist.getDayInSocialistHistory()
        rate = CoJoTheCapitalist.getCapitalisteRateForSocialistDate(rate_date)
        foreign_price = round(float(price) * float(1+(inflation_rate/100.0)) * float(rate['rate']), 2)
        return "{foreign_price} {currency} (taxa de {rate_date})".format(foreign_price=foreign_price,
                                                                         currency=rate['currency'],
                                                                         rate_date=rate_date.strftime("%Y-%m-%d"))
    @staticmethod
    def getDayInSocialistHistory():
        # days since 1999-01-04
        first_date = date(1999, 1, 4)
        max_days = date.today() - first_date
        days_delta = round(uniform(0, max_days.days), 0)
        return first_date + timedelta(days=days_delta)

    @staticmethod
    def getCapitalisteRateForSocialistDate(rate_date):
        uri = "https://api.exchangeratesapi.io/{rate_date}".format(rate_date=rate_date.strftime("%Y-%m-%d"))
        r = requests.get(uri)
        if r.status_code == 200:
            exchange_rates = r.json()
            currency = choice(list(exchange_rates['rates'].keys()))
            rate = exchange_rates['rates'][currency]
            return {"currency": currency, "rate": rate}
        else:
            return {"currency": "EUR", "rate": 1}

if __name__ == '__main__':
    ## run the thing
    tacm = TheAwesomeCoupleMixer()
    wonder_couples = tacm.getWonderCouples(emails=s.couples)
    tipf = TheIntrepidPriceFinder(min_price=s.min_price, max_price=s.max_price)
    price = tipf.getThePriceForHappiness()

    from_email_pwd = getpass.getpass()

    tfm = TheFabulousMailer(smtp_server=s.smtp_server, smtp_port=s.smtp_port,
                            from_email=s.from_email, from_email_pwd=from_email_pwd,
                            subject=s.subject, price=price, inflation_rate=s.inflation_rate)
    tfm.performLegendarySending(wonder_couples=wonder_couples)
