lista = [
    "PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
    "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
    "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"
]

kategoriat = ["Pienlaitteet", "Kylmälaitteet", "Sekoittimet"]

for rivi in lista:
    jako = rivi.split("_")
    merkki = jako[0]
    nimi = jako[1]
    malli = jako[2]
    paiva = jako[5]
    kk = jako[4]
    vuosi = jako[3]
    katenum = int(jako[7]) - 1

    print(f"Valmistaja: {merkki}\nNimi ja Malli: {nimi}({malli})\nKategoria: {kategoriat[katenum]}\nLisäyspäivämäärä: {paiva}.{kk}.{vuosi}\n")