from math import pi

jatka = "k"
while jatka == "k":
    sade = int(input("Anna säde: "))
    pinta = pi * sade ** 2
    print("Ympyrän pinta-ala on: {:.2f}".format(pinta))
    jatka = input("Haluatko jatkaa (k/e)? ")
    # PALAUTE break on tässä turha, koska suoritus katkeaa jo sillä, ett' jatka on erisuurin kuin e
    if jatka == "e":
        print("jorma")
        break

