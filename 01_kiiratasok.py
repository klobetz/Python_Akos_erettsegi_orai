#képernyőre kiíratás


print("Első programom!")            #futtatáshoz shift+ctrl+F10
print('Első programom!')            #vagy így
print('Első programom! "idézet" ')
#print("Első programom! "idézet" ")            #ez íg hibás kiíratás SyntaxError:

#több sorbn való kiíratás?
print('második '                 #ez így egy sorban írja ki a kiíratást
      'programom! de nem jó')
#ezt használjuk több sorhoz!
print("""első sor
valami
valami kettő
""")

#érték típusok
15          #int
"szöveg"    #str (sztring)
3.15        #float (lebegő pontos)

#válltozó
a = 0
print(a)
a = 15                  #int típus (szám)
print(type(a))
print(a)
szoveg = ""             #üres sztring típusú változó

szoveg = "Ez egy szöveg!"
print(type(szoveg))
print(szoveg)

#változó értéknövelés
print("-"*50)
b = 0
print(b)

b = b+1     #sztenderd
print(b)

b += 10
print(b)

b *= 5
print(b)

#b =* 50          #ez nem jó így nem használjuk

#változó típusának a megváltoztatása
print("-"*50)
nap = "süt a nap"
print(type(nap))
print(nap)
print()
nap = 2022
print(type(nap))
print(nap)

#beépített függvény len() változóben tárolt elemek hosszának a kiíratása
print("-"*50)
nev = "Klobetz Ákos"
hossz = len(nev)
print(hossz)
#egyben
print(len(nev))

#változó művelet összeadások
print("-"*50)
c = 8
d = 5
e = c+d
print(e)

#kiítarás szöveggel:
print("Az e változóm értéke: e")
print("Az e változóm értéke: " + str(e))
print("Az e változóm értéke:", e)
print(f"Az e változóm értéke: {e}")
print(f"Az {e} ami az e változó értéke.") #f sztring változó beillesztése

#típuskonverzió:
#ezek a sorok nem egyenlőek a változók típusaival
int(15)
float(15)
str(15)


#műveletek:

#összeadás (+)
#kivonás (-)
#szorzás (*)
#hatváynozás (**)
#osztás maradéka (%)
#osztás ( (/) vagy (//))
print("-"*50)
f = e/3                 #maradékos osztás
print(f)

f = e//3                #egészre kerekített
print(f)

g = e**2                #hatványozás
print(g)

h = e%d                 #osztás maradéka
print(h)

h = 13%5
h = 15%22
print(h)

#zárójelek
print("-"*50)
i = 5
i = 3*i+1
print(i)
#A zárójelek módosítják az eredményt
i = 5
i = 3*(i+1)
print(i)

#szöveg összefűzés a (+) jel segítségével
print("-"*50)
vnev = "Klobetz"
knev = "Ákos"
print(vnev + knev)            # ez így nem igazán jó
print(vnev+" "+knev)          #még egy üres karaktert hozzáadok
print("!"*50)

nev = vnev + knev
print(nev)
nev = f"{vnev} {knev}"
print(nev)

print("!"*50)
#de ez nem összefűzés (string interpoláció)
print(f"{vnev} {knev}")
print("!"*50)

print("-"*50)
#adatok bekérése a felhasználóktól!
# input("Kérek egy keresztnevet: ")
# print(input("Kérek egy keresztnevet: "))
# valasz = input("Kérek egy nevet: ")
# print(valasz)

# valaszvnev = input("Kérek egy vezetéknevet: ")
# valaszknev = input("Kérek egy keresztnevet: ")
#
# print(f"A kért adat: {valaszvnev} {valaszknev}")

#kérj be két számot és írasd ki az összegüket:

# valaszszam1 = int(input("kérek egy számot: "))
# valaszszam2 = int(input("kérek egy másik számot: "))
# print(f"A két szám összege: {valaszszam1 + valaszszam2}")

#lista létrehozása
lista = []        #üres lista
print(type(lista))
print(lista)

lista = [3, 5, 7, 4, 12, 54, 65]          # int lista
print(lista)
print(type(lista))

#lista adott elemének az elérése
lista = ["alma", "körte", "banán", "narancs"]   #sztring lista

print(lista[0])         #az első elem kiíratása
print(lista[-1])        #utolsó elem kiíratása
