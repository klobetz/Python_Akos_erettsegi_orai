#lista létrehozása:
ureslista = []
szamoklista = [51,32,3,74,5,68,73,448,649,410]
szoveglista = ["alma", "virág", "kutya","ember"]
listaalistaban = [4,5,8,3,[8,5,4,7,5,54]]
vegyeslista = ["szövg", 4,5,84,["Szövegek",5,7,4.6]]
#list kiíratása
print(ureslista,szoveglista,szamoklista,vegyeslista,listaalistaban)

#lista adott elemének az elérése:
print(szoveglista[1])

#lista elemeinek a kiírása:
for elem in szamoklista:
    print(elem)

#agy
print(*vegyeslista)

#keresés a lista elemein (in, not in)
print(32 in szamoklista) #True or False

#lista műveletek
osszead = szamoklista + szamoklista
print(osszead)

# szorzat:
szorzas = szamoklista * 2
print(szorzas)
print(szamoklista)
for szorzat in szamoklista:
    print(szorzat*2, end=", ")
print()
print(szamoklista)

#szeletelés:
print(szamoklista[5:9])

#elemek módosítása:
print(szoveglista)
szoveglista[2] = "FALIÓRA"
print(szoveglista)
#beszúr:
szoveglista[1:1] = "kutyA"
print(szoveglista)
#törlés:
print(szamoklista)
del szamoklista[2]
print(szamoklista)
#hozzáfűz:
szamoklista.append(3)
print(szamoklista)

#műveletek
for i in range(len(szamoklista)):
    print(i)

for i in range(len(szamoklista)):
    print(f"{i} => {szamoklista[i]*2}")

#szebben:
print("*"*50)
for index, elem in enumerate(szamoklista):
    print(f"{index} => {elem*2}")

#listametodusok