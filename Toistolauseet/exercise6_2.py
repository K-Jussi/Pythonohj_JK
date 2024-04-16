
jatka = True

while jatka:
    luku = int(input("Minkä kertotaulun haluat tulostaa(1-10, 0 lopettaa ohjelman): "))
    if not luku <= 10 and luku >= 1 :
        luku = int(input("Väärä luku, anna uusi (1-10): "))
    elif luku == 0:
        jatka = False
        break

    for i in range(1, 11):
        print(luku, 'x', i, '=', luku * i)
