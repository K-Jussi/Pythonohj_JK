import functions

valinta = int(input("Valitse toimenpide (1 = Laatikon tilavuus, 2 = Pallon tilavuus, 3 = Putken tilavuus, 0 = Lopettaa ohjelman): "))

if valinta == 1:
    leveys = float(input("Anna leveys: "))
    korkeus = float(input("Anna korkeus: "))
    syvyys = float(input("Anna syvyys: "))
    vastaus = functions.kuutiot(leveys, korkeus, syvyys)
    print(vastaus)

if valinta == 2:
    sade = int(input("Anna säde: "))
    vastaus = functions.pallon_tilavuus(sade)
    print(vastaus)

if valinta == 3:
    sade = int(input("Anna säde: "))
    pituus = int(input("Anna pituus: "))
    vastaus = functions.putken_tilavuus(sade, pituus)
    print(vastaus)




