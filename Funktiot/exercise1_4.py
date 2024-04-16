import functions

osallistujat_str = input("Syötä tapahtuman osallistujat pilkulla eroteltuna: ")

osallistujat = osallistujat_str.split(",")

osallistujat = [p.strip() for p in osallistujat]

functions.show_numbered_list("Ilmoittautumisjärjestys: ", osallistujat)

osallistujat.sort()

functions.show_numbered_list("Aakkosjärjestys etunimen perusteella: ", osallistujat)

osallistujat = [" ".join(reversed(p.split(" "))) for p in osallistujat]
osallistujat.sort()

functions.show_numbered_list("Aakkosjärjestys sukunimen perusteella: ", osallistujat)
