lista = ["Rooma", "Ateena", "Tukholma", "Lontoo", "Dublin", "Pariisi"]
num = len(lista)
for rivi in range(num):
    lista.sort(reverse=False)
    maa = lista[rivi]
    print(f"{rivi + 1}-{maa}")