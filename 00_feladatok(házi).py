# Van egy bizonyos összegünk, amelyből számlákat szeretnénk kifizetni, de maximum tízet.
# Kérje be a rendelkezsszeget, majd sorban a számlaösszegeket!
# Ha a számlák száma eléri a tízet, vagy az adott számlára már nincs pénz, adjon a program egy figyelmeztetést!
# Végül írja ki, hány számlát sikerült kifizetni, és mennyi a ténylegesen kifizetendő összeg!

osszespenzem = int(input("mennyi pénzem van?: "))
befizetettszamladb = 0
osszszamla = 0
for elem in range(10):
    kertszamla = int(input("Kérem a számlát: "))
    osszszamla += kertszamla
    if osszespenzem == kertszamla or osszszamla <= osszespenzem and osszespenzem > kertszamla:
        befizetettszamladb += 1
    else:
        print("Nincs elég pénzem!")
        osszszamla -= kertszamla
        break

print(f"a befizetett számlák {befizetettszamladb} db és az összeg: {osszszamla}")

