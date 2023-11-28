#!usr/bin/python
# -*- coding: utf-8 -*-
#

from random import choice, uniform
import smtplib
import requests
from email.mime.text import MIMEText
from datetime import date, timedelta
import getpass
from youtubesearchpython import Search as yt_search
import settings_2023 as s



class TheWonderCouple:
    def __init__(self, gifter_email, gifted_email, joke, chuck_fact):
        self.gifter_email = gifter_email
        self.gifted_email = gifted_email
        self.joke = joke
        self.chuck_fact = chuck_fact


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
            joke = CoJoTheEntertainer.getFatherTheDadJokeriny()
            chuck_fact = CoJoTheEntertainer.getChuckNorrisTruthOfLifeFact()
            twc = TheWonderCouple(emails[gifter], emails[gifted], joke, chuck_fact)
            self.wonder_couples.append(twc)

    def getWonderCouples(self, emails):
        self.magicMixer(emails)
        return self.wonder_couples


class TheFabulousMailer:
    def __init__(self, smtp_server, smtp_port, from_email, from_email_pwd,
                 subject):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.from_email_pwd = from_email_pwd
        self.subject = subject

    def performLegendarySending(self, wonder_couples):
        # server = smtplib.SMTP_SSL(self.smtp_server, 465)#self.smtp_port)
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.from_email, self.from_email_pwd)
        for wonder_couple in wonder_couples:
            print("Sending to {gifter_email}".format(gifter_email=wonder_couple.gifter_email))
            to_email = wonder_couple.gifter_email
            msg_text = """
                Sois o casal {gifter_email}
                Ides ofertar presentes ao casal {gifted_email}

                O Grande {beast} Flexitariano escolheu esta banda sonora para vós:
                {chosen_song}

                And I say to you: {joke}

                'mai nada!

                And always remember this close to your heart: {chuck_fact}

                """.format(gifter_email=wonder_couple.gifter_email,
                           gifted_email=wonder_couple.gifted_email,
                           beast=TheWildernessExplorer.getMightyBeast(),
                           chosen_song=CoJoTheMusicologist.getPhenomenalSoundtrack(),
                           joke=wonder_couple.joke,
                           chuck_fact=wonder_couple.chuck_fact
                           )
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


class TheWildernessExplorer:
    @staticmethod
    def getMightyBeast():
        r = requests.get('https://gist.githubusercontent.com/rphenriques/23f353967b4052d44eb229f99221345c/raw/6e46db8f5c27cb18fd1dfa50c7c921a0fbacbad0/animals.json')
        if r.status_code == 200:
            return choice(list(r.json()))
        else:
            return "CoupleMixer"


class CoJoTheEntertainer:

    @staticmethod
    def getFatherTheDadJokeriny():
        headers = {'Accept': 'application/json'}
        r = requests.get('https://icanhazdadjoke.com', headers=headers)
        if r.status_code == 200:
            the_line = r.json()
            return the_line['joke']
        else:
            return "No joke for you"

    @staticmethod
    def getChuckNorrisTruthOfLifeFact():
        r = requests.get('https://api.chucknorris.io/jokes/random')
        if r.status_code == 200:
            the_line = r.json()
            return the_line['value']
        else:
            return "No joke for you"


class CoJoTheMusicologist:
    @staticmethod
    def getPhenomenalSoundtrack():
        the_wonderfull_curated_list = [
            "https://www.youtube.com/watch?v=hvL1339luv0",
            "https://www.youtube.com/watch?v=kEPfM3jSoBw",
            "https://www.youtube.com/watch?v=5sNuDu4dE8Y",
            "https://www.youtube.com/watch?v=pXezLv_5RaY",
            "https://www.youtube.com/watch?v=NV0BgRFHGGA",
            "https://www.youtube.com/watch?v=mBw3qzf4s18",
            "https://www.youtube.com/watch?v=uDrdZM1iGrc"]

        the_wonderfull_curated_list.append(CoJoTheMusicologist.getOutstandingSongs())

        return choice(the_wonderfull_curated_list)

    @staticmethod
    def getOutstandingSongs():
        s_res = yt_search("rick astley never gonna give you up", limit=3)
        return [pos['link'] for pos in s_res.result()['result']]


if __name__ == '__main__':
    ## run the thing
    tacm = TheAwesomeCoupleMixer()
    wonder_couples = tacm.getWonderCouples(emails=s.couples)
    from_email_pwd = getpass.getpass()

    tfm = TheFabulousMailer(smtp_server=s.smtp_server, smtp_port=s.smtp_port,
                            from_email=s.from_email, from_email_pwd=from_email_pwd,
                            subject=s.subject)
    tfm.performLegendarySending(wonder_couples=wonder_couples)
