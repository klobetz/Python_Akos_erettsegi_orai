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