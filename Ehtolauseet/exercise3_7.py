tyyppi = int(input("Onko lähetys kirje vai paketti(1 = kirje, 2 = paketti): "))
paino = int(input("Anna lähetyksen paino grammoina: "))
lisamaksu = 0

if 200 <= paino <= 500:
    if tyyppi == 1:
        kerroin = 0.04
    else:
        kerroin = 0.08
elif paino > 500:
    if tyyppi == 1:
        kerroin = 0.07
        lisa = input("Mahtuuko kirje postilaatikkoon (k/e)? ")
        if lisa == "e":
            lisamaksu = 2
    else:
        kerroin = 0.14
else:
    kerroin = 0

if tyyppi == 1:
    hinta = 0.5 + (paino//100 * kerroin) + lisamaksu
else:
    hinta = 2 + (paino//100 * kerroin)

txt = "Lähetyksen postimaksu on {:.2f}€"
print(txt.format(hinta))

