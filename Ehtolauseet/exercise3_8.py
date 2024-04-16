ostokset = float(input("Anna ostosten summa: "))
opiskelija = input("Oletko opiskelija (k/e)? ")
kanta = input("Oletko kanta-asiakas (k/e)? ")

if kanta == "k":
    pisteet = int(input("Anna kanta-asiakas pisteet: "))

alennus = input("Anna alennuskoodi: ")
if alennus == "FALL23":
    ostokset = ostokset * 0.9
elif alennus == "BK2SCHOOL" and opiskelija == "k":
    ostokset = ostokset * 0.8

if kanta == "k":
    alepisteet = pisteet + (ostokset // 10 * 100)
    kantaale = (alepisteet // 1000) * 5
    ostokset = ostokset - kantaale

if ostokset < 100:
    ostokset = ostokset + 7.95

txt = "Tilauksen loppusumma on {:.2f}€"
print(txt.format(ostokset))

