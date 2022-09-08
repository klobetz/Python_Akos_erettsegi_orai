#feltételes végrehajtás

#két változó a kisebb mint a (b)

a = 225
b = 36

if a < b:
    #igaz ág
    print(f"az {a} szám kisebb mint a {b} szám")
else:
    #hamis ág
    print(f"Nem a {a} szám nem nagyobb a {b} számnál")

#kérjen be a felhasználótól egy számot és döntse el róla hogy az páros vagy páratlan
valasz = int(input("Kérek egy pozitív egész számot: "))
if valasz % 2 == 0:
    print("páros")
else:
    print("páratlan")

#kérjen be a felhasználótól egy számot és döntse el róla hogy pozitív vagy negatív
valasz = input("Kérek egy egész számot: ")
if int(valasz) > 0:
    print("pozitív")
else:
    print("negatív")

#beágyazott feltétel
valasz = input("Kérek egy egész számot: ")
if int(valasz) > 0:
    print("pozitív")
else:
    if int(valasz) == 0:
        print("a Szám 0-a")
    else:
        print("negatív")

#kérjen be a felhasználótól egy számot és döntse el róla hogy 0 és 10 közé esik vagy 10 nél nagyobb
valasz = int(input("Kérek egy pozitív egész számot: "))
if valasz > 0:
    if valasz<10:
        print(" a szám 0 és 10 közé esik")
    else:
        print("A szám 10-nél nagyobb")

if valasz > 0 and valasz < 10:
    print(" a szám 0 és 10 közé esik")
else:
    print("A szám 10-nél nagyobb")

#láncolt feltételes utasítás
#melyik a helyes válasz? az "a" "b" vagy a "c"
print("milyen színű a fű?")
valasz = input("('a' válasz) A fű kék\n('b' válasz) A fű zöld\n('c' válasz) A fű pios\nválasz: ")

#print("('a' válasz) A fű kék\n('b' válasz) A fű zöld\n('c' válasz) A fű pios")

if valasz == "a":
    print("A fű kék")
elif valasz == "b":
    print("A fű zöld")
elif valasz == "c":
    print("A fű pios")
else:
    print("rosz válasz")

