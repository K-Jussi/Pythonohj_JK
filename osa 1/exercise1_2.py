
hinta = float(input("Anna hinta ilman ALV:tä: "))

tulos = hinta * 1.24

txt = "Hinta ALV:n kanssa: {:.2f} "
print(txt.format(tulos))
