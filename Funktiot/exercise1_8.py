import functions

raha = float(input("Anna vaihdettava summa: "))
valuutta = int(input("Anna vaihdettavan valuutan tyyppi (1 = Dollari, 2 = Punta, 3 = Ruotsin kruunu, 4 = Euro): "))
vaihtovaluutta = int(input("Mihin valuuttaan vaihdetaan (1 = Dollari, 2 = Punta, 3 = Ruotsin kruunu, 4 = Euro): "))

tulos = functions.laske_valuutta(raha, valuutta, vaihtovaluutta)
print(format(tulos, ".2f"))
