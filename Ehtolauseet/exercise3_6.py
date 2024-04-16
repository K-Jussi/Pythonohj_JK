vuosi = int(input("Anna vuosiluku: "))
onkoKarkaus = bool
if vuosi % 400 == 0:
    onkoKarkaus = True
else:
    if vuosi % 100 == 0:
        onkoKarkaus = False
    elif vuosi % 4 == 0:
        onkoKarkaus = True
    else:
        onkoKarkaus = False

if onkoKarkaus:
    print("Karkausvuosi: Kyllä")
else:
    print("Karkausvuosi: Ei")