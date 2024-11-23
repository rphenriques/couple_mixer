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
import settings_2024 as s



class TheWonderCouple:
    def __init__(self, gifter_email, gifted_email, joke, chuck_fact, price, jolie_friend):
        self.gifter_email = gifter_email
        self.gifted_email = gifted_email
        self.joke = joke
        self.chuck_fact = chuck_fact
        self.price = price
        self.jolie_friend = jolie_friend


class TheAwesomeCoupleMixer:
    def __init__(self):
        self.wonder_couples = []

    def magicMixer(self, emails, price):
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
            jolie_friend = CoJoTheEntertainer.getCoolFriend()
            twc = TheWonderCouple(emails[gifter], emails[gifted], joke, chuck_fact, price, jolie_friend)
            self.wonder_couples.append(twc)

    def getWonderCouples(self, emails, price):
        self.magicMixer(emails, price)
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

                O Grande {beast} Flexitariano aconselha este tema para o momento da escolha:
                {chosen_song}

                O valor é de {price}. Mais coisa ou menos.

                And I say to you: {joke}

                'mai nada!

                And always remember this close to your heart: {chuck_fact}

                Look at me, I'm a {jolie_friend}

                """.format(gifter_email=wonder_couple.gifter_email,
                           gifted_email=wonder_couple.gifted_email,
                           beast=TheWildernessExplorer.getMightyBeast(),
                           chosen_song=CoJoTheMusicologist.getPhenomenalSoundtrack(),
                           joke=wonder_couple.joke,
                           chuck_fact=wonder_couple.chuck_fact,
                           price=wonder_couple.price,
                           jolie_friend=wonder_couple.jolie_friend
                           )
            message = MIMEText(msg_text)
            message['From'] = self.from_email
            message['To'] = to_email
            message['Subject'] = self.subject
            server.sendmail(self.from_email, to_email, message.as_string())
        server.quit()
        print("All done!")


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

    @staticmethod
    def getCoolFriend():
        r = requests.get('https://api.capy.lol/v1/capybara?json=true')
        if r.status_code == 200:
            the_line = r.json()
            return the_line['data']['url']
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
            "https://www.youtube.com/watch?v=uDrdZM1iGrc",
            "https://www.youtube.com/watch?v=w3rQ3328Tok",
            "https://www.youtube.com/watch?v=W85oD8FEF78",
            "https://www.youtube.com/watch?v=BqYyE2JNMfg"]

        the_wonderfull_curated_list.append(CoJoTheMusicologist.getOutstandingSongs())

        return choice(the_wonderfull_curated_list)

    def getOutstandingSongs():
        s_res = yt_search("rick astley never gonna give you up", limit=3)
        return [pos['link'] for pos in s_res.result()['result']]

class TheIntrepidPriceFinder:
    @staticmethod
    def getThePriceForHappiness(min_price, max_price):
        price = round(uniform(min_price, max_price), 2)
        return str(price)

if __name__ == '__main__':
    ## run the thing
    tacm = TheAwesomeCoupleMixer()
    wonder_couples = tacm.getWonderCouples(emails=s.couples, price=TheIntrepidPriceFinder.getThePriceForHappiness(s.min_price, s.max_price))
    from_email_pwd = getpass.getpass()

    tfm = TheFabulousMailer(smtp_server=s.smtp_server, smtp_port=s.smtp_port,
                            from_email=s.from_email, from_email_pwd=from_email_pwd,
                            subject=s.subject)
    tfm.performLegendarySending(wonder_couples=wonder_couples)
