sentit = int(input("Anna 1-100 senttiä: "))

snt50 = sentit // 50

sentit = sentit % 50
snt20 = sentit // 20

sentit = sentit % 20
snt10 = sentit // 10

sentit = sentit % 10
snt5 = sentit // 5

sentit = sentit % 5
snt2 = sentit // 2

sentit = sentit % 2
snt1 = sentit // 1

print("50 snt kolikoita {}kpl\n20 snt kolikoita {}kpl\n10 snt kolikoita {}kpl\n5 snt kolikoita {}kpl\n2 snt kolikoita {}kpl\n1 snt kolikoita {}kpl".format(snt50, snt20, snt10, snt5, snt2, snt1))
