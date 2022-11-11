# # Van egy bizonyos összegünk, amelyből számlákat szeretnénk kifizetni, de maximum tízet.
# # Kérje be a rendelkezsszeget, majd sorban a számlaösszegeket!
# # Ha a számlák száma eléri a tízet, vagy az adott számlára már nincs pénz, adjon a program egy figyelmeztetést!
# # Végül írja ki, hány számlát sikerült kifizetni, és mennyi a ténylegesen kifizetendő összeg!
import math
#
# osszespenzem = int(input("mennyi pénzem van?: "))
# befizetettszamladb = 0
# osszszamla = 0
# for elem in range(10):
#     kertszamla = int(input("Kérem a számlát: "))
#     osszszamla += kertszamla
#     if osszespenzem == kertszamla or osszszamla <= osszespenzem and osszespenzem > kertszamla:
#         befizetettszamladb += 1
#     else:
#         print("Nincs elég pénzem!")
#         osszszamla -= kertszamla
#         break
#
# print(f"a befizetett számlák {befizetettszamladb} db és az összeg: {osszszamla}")
#
# #3 szá írasd ki a legkisebbet és a legnagyobbat
# valasz = int(input("szám1: "))
# valasz2 = int(input("szám2: "))
# valasz3 = int(input("szám3: "))
#
# print(f"legkisebb: {min(valasz,valasz2,valasz3)}")
# print(f"legkisebb: {max(valasz,valasz2,valasz3)}")
#
# szam = math.pi
# szam3 = 3.68
# print(f"{round(szam,2)}")
# print(f"{szam3:.3f}")
# print(f"{szam3:.2f}")
# print(f"{math.ceil(szam3)}")
# print(f"{math.floor(szam3)}")

##példa részek a feladat megoldáshoz
# szoveg = "gyümölcs"
# db = 0
# valasz = input("kérek egy karaktert: ")
#
# for elem in szoveg:
#     print(elem)
#     db +=1
#     # if valasz == elem:
#     #     print("van találat!")
# print(db)
#
# lista = ["gyümölcs", "ü"]
# print(lista)
# for i in lista:
#     if valasz == i:
#         print("van találat!")
#
# if valasz in szoveg:
#     pass
# else:
#     pass

# lista = [0,1]
# print(lista)
# lista.append(5)
# print(lista)

import random, math

random
r = [random.randrange(1,101,1) for elem in range(100)]
print(r)

szamok = []
for elem in range(10):
    elem = random.randrange(1,101,1)
    szamok.append(elem)
print(len(szamok))
print(len(r))
print(szamok)
pi = math.pi
print(f"{pi:.2f}")