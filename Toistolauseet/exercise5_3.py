from math import pi

jatka = "k"
while jatka == "k":
    sade = int(input("Anna säde: "))
    pinta = pi * sade ** 2
    print("Ympyrän pinta-ala on: {:.2f}".format(pinta))
    jatka = input("Haluatko jatkaa (k/e)? ")
    if jatka == "e":
        break

