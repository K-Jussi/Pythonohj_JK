pisteet = int(input("Anna pistemäärä: "))

if pisteet <= 50 and pisteet >= 0:
    print(0)
elif pisteet > 50 and pisteet <= 60:
    print(1)
elif pisteet > 60 and pisteet <= 70:
    print(2)
elif pisteet > 70 and pisteet <= 80:
    print(3)
elif pisteet > 80 and pisteet <= 90:
    print(4)
elif pisteet > 90 and pisteet <= 100:
    print(5)
else:
    print("Pistemäärä ei ole mahdollinen")
