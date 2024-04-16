raha = int(input("Anna rahaa: "))
ostokset = int(input("Ostosten hinta: "))

if raha > ostokset:
    vaihto = raha - ostokset
    print("Kiitos. Annetaan takaisin {} €".format(vaihto))

else:
    lisaa = int(input("Rahat eivät riitä, anna lisää rahaa: "))
    uusiraha = raha + lisaa

    if uusiraha > ostokset:
        vaihto = uusiraha - ostokset
        print("Kiitos. Annetaan takaisin {} €".format(vaihto))

    else:
        print("Sinulla ei ole tarpeeksi rahaa.")
