autoklista = []
with open("txt_allomanyok/autok.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")

        nap = int(sor[0])
        ido = sor[1]
        rendszam = sor[2]
        azonosito = int(sor[3])
        km = int(sor[4])
        kibehjtas = int(sor[5])
        #adat = [nap,ido,rendszam,azonosito,km,kibehjtas]
        #autoklista.append(adat)
        autoklista.append([nap,ido,rendszam,azonosito,km,kibehjtas])


# for elem in autoklista:
#     print(elem[1])
#
# for nap,ido,rendszam,azonosito,km,kibehjtas in autoklista:
#     print(rendszam)

#2.feladat
for nap,ido,rendszam,azonosito,km,kibehjtas in autoklista:
     if kibehjtas == 0:
         autorendszam = rendszam
         adottnap = nap

print(f"2. feladat\n{adottnap}. nap rendszám: {autorendszam}")

# for elem in autoklista:
#     if elem[5] == 0:
#         autorendszam2 = elem[2]
#         adottnap2 = elem[0]
# print(f"2. feladat\n{adottnap2}. nap rendszám: {autorendszam2}")

#hány sort tartalmaz a fájl?
print(f"A fájl {len(autoklista)} sort tartalmaz")

print("3.feladat")
#valasz = input("Nap: ")
valasz = 4
print(f"Forgalom a(z) {valasz}. napon: ")
for nap,ido,rendszam,azonosito,km,kibehjtas in autoklista:
    if nap == valasz:
        if kibehjtas == 0:
            print(f"{ido} {rendszam} {azonosito} ki")
        else:
            print(f"{ido} {rendszam} {azonosito} be")

#4.feladat:
dbki = 0
dbbe = 0
for nap,ido,rendszam,azonosito,km,kibehjtas in autoklista:
    if kibehjtas == 0:
        dbki += 1
    else:
        dbbe += 1
print(f"4. feladat\nA hónap végén {dbki-dbbe} autót nem hoztak vissza. ")

#5.feladat:
rendszamoklista = []
for nap,ido,rendszam,azonosito,km,kibehjtas in autoklista:
    if rendszam not in rendszamoklista:
        rendszamoklista.append(rendszam)
rendszamoklista.sort()              #ebben az esetben az eredeti lista is megváltozik!!!!
#print(sorted(rendszamoklista))     #ebben az esetben csak a kiíratás idejéig lesz rendezve a listám!!!!!!
#print(rendszamoklista)             #visszanyúlhatok az eredeti listára ami nincs sorba rendezve!!!

for elem in rendszamoklista:
    megtettkm = []
    for nap, ido, rendszam, azonosito, km, kibehjtas in autoklista:
        if elem == rendszam:
            megtettkm.append(km)
        #print(f"{rendszam} {megtettkm}")
    kezdokm = megtettkm[0]
    utolsokm = megtettkm[-1]
    megtettkm = utolsokm-kezdokm
    print(f"{elem} {megtettkm} km")

#6.feladat:
leghosszabbut = 0
for elem in rendszamoklista:
    for nap, ido, rendszam, azonosito, km, kibehjtas in autoklista:
        if elem == rendszam:
            if kibehjtas == 0:
                kezdokm = km
            else:
                uthossza = km-kezdokm
                #print(rendszam,uthossza)
                if leghosszabbut<uthossza:
                    leghosszabbut = uthossza
                    dolgoadat = azonosito
print(f"Leghosszabb út: {leghosszabbut} km, személy: {dolgoadat} ")

#7.feladat:
#valasz = input("Rendszám: ")
valasz = "CEG304"
with open(f"kiiratas/{valasz}_menetlevel.txt", "w", encoding="utf8") as f:
    for nap, ido, rendszam, azonosito, km, kibehjtas in autoklista:
        if rendszam == valasz:
            if kibehjtas == 0:
                f.writelines(f"{azonosito}\t {nap}. {ido}\t {km}km\t")
            else:
                f.writelines(f"{nap}. {ido}\t {km}km\n")
print(f"7. feladat:\nRendszám: {valasz}\nA menetlevél kész.")