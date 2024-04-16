tunnit = int(input("Syötä viikon työtunnit: "))
palkka = float(input("Syötä tuntipalkkasi: "))

if tunnit <= 40:
    ansiot = tunnit * palkka

else:
    normipalkka = 40 * palkka
    ylityop = (tunnit - 40) * (palkka * 1.5)
    ansiot = normipalkka + ylityop

txt = "Viikon ansiosi ovat: {:.2f}"
print(txt.format(ansiot))