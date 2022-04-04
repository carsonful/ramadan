import os
from dotenv import load_dotenv

load_dotenv()


user = os.environ['user']

sid = os.environ['SID']

csrf = os.environ['CSRF']


carson = os.environ['carson']

people = []

evren = os.environ['evren']
alara = os.environ['alara']
amin = os.environ['amin']

people.append(evren.split(","))
people.append(alara.split(","))
people.append(amin.split(","))
people.append(carson.split(","))


def peoples():
    return people