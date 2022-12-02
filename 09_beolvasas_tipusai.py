#01 beolvasás
#sima soronként
import sys

autoklista = []
with open("txt_allomanyok/01_beolvasas.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")

        nap = int(sor[0])
        ido = sor[1]
        rendszam = sor[2]
        azonosito = int(sor[3])
        km = int(sor[4])
        kibehajtas = int(sor[5])
        autoklista.append([nap, ido, rendszam, azonosito, km, kibehajtas])
for nap, ido, rendszam, azonosito, km, kibehajtas in autoklista:
    print(rendszam)

#02 beolvasás
#első sor kivétele
versenylista = []
with open("txt_allomanyok/02_beolvasas.txt", encoding="utf8") as f:
    helyesmegoldas = f.readline()
    for adat in f:
        sor = adat.strip().split(" ")

        versenyzoazon = sor[0]
        versenyzovalasz = sor[1]
        versenylista.append([versenyzoazon,versenyzovalasz])
for versenyzoazon,versenyzovalasz in versenylista:
    print(versenyzoazon)
print(helyesmegoldas)

#03 beolvasás:
#bizonyos soronként ismétlődő sononkénti beolvasás pl 4x
tantargyfelosztaslista = []
with open("txt_allomanyok/03_beolvasas.txt", encoding="utf8") as f:
    while True:
        nev = f.readline().strip()
        if not nev:
            break
        tantargy = f.readline().strip()
        osztaly = f.readline().strip()
        oraszam = int(f.readline().strip())
        tantargyfelosztaslista.append([nev,tantargy,osztaly,oraszam])

for nev,tantargy,osztaly,oraszam in tantargyfelosztaslista:
    print(nev)
# nevek kiválogatása az eredeti listából
print(len(tantargyfelosztaslista))
tanarlista = []
for nev,tantargy,osztaly,oraszam in tantargyfelosztaslista:
    if nev not in tanarlista:
        tanarlista.append(nev)
print(len(tanarlista))

#04 beolvasás
#egy adott karkterig ismétlődik a beolvasás pl "#"
naplolista = []
with open("txt_allomanyok/04_beolvasas.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")

        if sor[0] == "#":
            honap = sor[1]
            nap = sor[2]
            #naplolista.append([honap, nap])
        else:
            nev = sor[0]+" "+sor[1]
            hianyzas = sor[2]
            naplolista.append([honap, nap, nev, hianyzas])

print(naplolista)

for honap,nap,nev,hianyzas in naplolista:
    if honap == "01" and nap == "17":
        print(nev)