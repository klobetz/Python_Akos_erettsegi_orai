#Beolvasás
with open("txt_allomanyok/nevek_sima.txt", encoding="utf8") as file:
    sorok = file.read()

print(sorok)
print(type(sorok))

#beolvasás és darabolás listába
with open("txt_allomanyok/nevek_sima.txt", encoding="utf8") as f:
    sorok2 = f.read()
    lista = sorok2.split()          #split => darabol

print(lista)
print(type(lista))
print("*"*50)

for elem in lista:
    print(elem)

#bizonyos sorok beolvasása
with open("txt_allomanyok/nevek_sima.txt", encoding="utf8") as f:
    f.readline().strip().split()         #strip => tisztítás az entereket tabulátorokat leszedi
    sor2 = f.readline().strip()
    sor3 = f.readline().strip().split()

print(sor3)
print(len(sor3))
print(sor2)

neveklista = []
with open("txt_allomanyok/nevek_sima.txt", encoding="utf8") as f:
    elsosor = f.readline()      #kiveszem és tárolom az első sort
    for sor in f:
        adat = sor.strip().split()
        neveklista.append(adat)

print(neveklista)

#bejárás
for vezeteknev in neveklista:
    print(vezeteknev[0])
print(len(neveklista))

#kicsit egyszerűbben:
print("!"*50)
neveklista2=[]
with open("txt_allomanyok/nevek_sima.txt", encoding="utf8") as f:
    elsosor = f.readline()
    for adat in f:
        sor = adat.strip().split(" ")
        vnev = sor[0]
        knev = sor[1]
        neveklista2.append([vnev,knev])

for vnev,knev in neveklista2:
    print(vnev)


