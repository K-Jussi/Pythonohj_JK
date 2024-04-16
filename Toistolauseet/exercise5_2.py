sade = 0

for i in range(1, 13):
    syotto = float(input("Syötä kuukauden sademäärä: "))
    sade = sade + syotto
sadekesk = float(sade/12)
print("Vuoden keskimääräinen sademäärä {:.1f}".format(sadekesk))
