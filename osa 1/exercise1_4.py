annaminuutit = int(input("Anna minuutit: "))

tunnit = annaminuutit // 60
minuutit = annaminuutit % 60

print("{}h {}min".format(tunnit, minuutit))