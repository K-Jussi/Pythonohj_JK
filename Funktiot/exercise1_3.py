serial = input("Anna ISSN sarjanumero: ")

from functions import *
magazine_serial_check(serial)

if magazine_serial_check(serial):
    print("Oikea ISSN sarjanumero")
else:
    print("Väärä ISSN sarjanumero")