lampotila = int(input("Anna lämpöasteet: "))

if lampotila <= 10:
    print("Kylmää")

elif lampotila >= 11 and lampotila <= 15:
    print("Koleaa")

elif lampotila >= 16 and lampotila <= 20:
    print("Normaali lämpötila")

elif lampotila >= 21 and lampotila <= 25:
    print("Lämmintä")

elif lampotila >= 26 and lampotila <= 30:
    print("Hellettä")

else:
    print("Et oo tosissas!!!")

