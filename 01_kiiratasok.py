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

#zárójelek

#szöveg összefűzés

#adatok bekérése a felhasználóktól!
