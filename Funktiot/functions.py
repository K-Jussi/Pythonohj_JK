import math
import pprint
import random

def show_personal_info():
    print("Matti Meikäläinen \nSodankylä\nOhjelmistosuunnittelija")


def count_seconds(hours, minutes, seconds):

    return hours * 60**2 + minutes * 60 + seconds


def magazine_serial_check(serial):
    newserial = serial.replace("-", "")
    if serial[4] == "-":
        if len(newserial) == 8:
            if newserial.isnumeric():
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def show_numbered_list(title, data):
    print("\n" + title)
    num = len(data)
    for i in range(num):
        item = data[i]
        print(f"{i + 1}-{item}")


def kuutiot(leveys, korkeus, syvyys):
    tulos = leveys * korkeus * syvyys
    return format(tulos, ".2f")


def pallon_tilavuus(sade):
    tulos = 4 * math.pi * sade**3 / 3
    return format(tulos, ".2f")


def putken_tilavuus(sade, pituus):
    tulos = math.pi * sade**2 * pituus
    return format(tulos, ".2f")


def arvo():
    lottonumerot = []
    for i in range(0, 9):
        numero = random.randint(1, 40)
        while numero in lottonumerot:
            numero = random.randint(1, 40)

        lottonumerot.append(numero)

    return lottonumerot

def laske_valuutta(raha, valuutta, vaihtovaluutta):
    tulos = float

    if valuutta == 1:
        rahatemp = raha / 1.1
        if vaihtovaluutta == 2:
            tulos = rahatemp * 0.9
        elif vaihtovaluutta == 3:
            tulos = rahatemp * 11.8
        else:
            tulos = rahatemp

    elif valuutta == 2:
        rahatemp = raha / 0.9
        if vaihtovaluutta == 1:
            tulos = rahatemp * 1.1
        elif vaihtovaluutta == 3:
            tulos = rahatemp * 11.8
        else:
            tulos = rahatemp

    elif valuutta == 3:
        rahatemp = raha / 11.8
        if vaihtovaluutta == 1:
            tulos = rahatemp * 1.1
        elif vaihtovaluutta == 2:
            tulos = rahatemp * 0.9
        else:
            tulos = rahatemp

    else:
        rahatemp = raha
        if vaihtovaluutta == 1:
            tulos = rahatemp * 1.1
        elif vaihtovaluutta == 2:
            tulos = rahatemp * 0.9
        else:
            tulos = rahatemp * 11.8

    return tulos


def keskuksetsorted(keskukset):
    keskukset1 = sorted(keskukset, key=lambda i: (i["city"], i["company"]))
    pprint.pprint(keskukset1)
