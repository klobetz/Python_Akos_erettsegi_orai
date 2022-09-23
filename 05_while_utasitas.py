# valasz = int(input("kérek egy számot: "))
# osszeg = 0
# db = 1
# while db <= valasz:
#     osszeg += db
#     db += 1
# print(osszeg)
#
# #ugyan ezt meg lehet csinálni for-ral de valamit nem! :D
# print("-"*50)
# osszeg2 = 0
# for i in range(valasz+1):
#     osszeg2 += i
#     #print(i)
# print(osszeg2)
#
# #Hátul tesztelős ciklus
# #a python-ban ezt az if és break használatával készítjük el. Másik nyelvnél do while
# while True:
#     jelszo = input("Kérem a jelszót: ")
#     jelszoujra = input("Jelszó megerősitése: ")
#     if jelszo == jelszoujra:
#         print("Ok! Köszönöm!")
#         break
#     print("A két jelszó nem egyezik próbáld újra!")
#
# #Középen tesztelős ciklus(if és break használatával)
# osszeg3 = 0
# while True:
#     valsz = input("Kérek egy számot! (Az enter leütésével megszakíthatod a folyamatot)\nA szám: ")
#     if valsz == "":
#         break
#     osszeg3 += int(valsz)
# print(f"A bekért számok összege: {osszeg3}")
#
#bekért adat ellenőrzése:
while True:
    try:
        valsaz = int(input("kérek egy számot:"))
    except ValueError:
        print("NEM SZÁM")
    else:
        print(f"ok! A beírt szám: {valsaz}")
        break

valaszszoveg = input("Kérek egy szöveget: ")
print(valaszszoveg.isdigit())

while valaszszoveg.isdigit() == True:
    valaszszoveg = input("Nem szöveget írtál be!\nKérek egy szöveget: ")
print("köszönöm!")


valaszszam = input("kérek egy számot:")
while valaszszam.isdigit() == False:
    valaszszam = input("NEM SZÁM\nKérek egy számot: ")
print("köszönöm!")