
jatka = True
vuosi = 2023

while jatka:
    alkhinta = int(input("Syötä alkuperäinen hinta: "))
    vmvuosi = int(input("Syötä valmistusvuosi: "))
    kmlukema = int(input("Syötä ajetut kilometrit: "))
    hintakat = int(input("Syötä hintakategoria(1 tai 2): "))
    tuontiauto = input("Onko kyseessä tuontiauto (k/e): ")

    ika: int = vuosi - vmvuosi
    hinnoittelu = kmlukema / ika
    uusihinta = 0
    tarkhinta = 0

    if hintakat == 1:
        if hinnoittelu < 30000:
            if ika <= 5:
                vahpro = 0.95
            elif ika >= 6:
                vahpro = 0.95
                vahpro2 = 0.97
        elif hinnoittelu >= 30000:
            if ika <= 5:
                vahpro = 0.93
            elif ika >= 6:
                vahrpo = 0.93
                vahpro2 = 0.96
        tarkhinta = alkhinta * 0.18

    if hintakat == 2:
        if hinnoittelu < 30000:
            if ika <= 5:
                vahpro = 0.92
            elif ika >= 6:
                vahpro = 0.92
                vahpro2 = 0.95
        elif hinnoittelu >= 30000:
            if ika <= 5:
                vahpro = 0.9
            elif ika >= 6:
                vahpro = 0.9
                vahpro2 = 0.93
        tarkhinta = alkhinta * 0.12

    if ika <= 5:
        uusihinta = alkhinta * (vahpro ** ika)
    else:
        uusihinta = alkhinta * (vahpro ** 5) * (vahpro2 ** (ika - 5))

    if tarkhinta >= uusihinta:
        tarkhinta = uusihinta
    if tuontiauto == "k":
        uusihinta = uusihinta * 1.24

    print("Lopullinen hinta on: ", uusihinta)
    kysjatka = input("Haluatko jatkaa(k/e): ")
    if kysjatka == "e":
        jatka = False
    else:
        jatka = True



