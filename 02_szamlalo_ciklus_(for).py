print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

print("-"*50)
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end=" ")

#ugyan ez változóban tárolva a listaelemeket
print()
print("-"*50)
lista = [1,2,3,4,5,6,7,8,9,10,11]

for i in lista:
    print(i, end=" ")

print()
print("-"*50)

for i in [1,2,3,4]:
    print("szeretek programozni")

#range használata
for elem in range(0,11,1):
    print(elem)

for elem in range(10):
    print(elem, end=" ")

print()
for elem in range(2):
    print("szeretk programozni")

#egy sorban az egész:
print(*range(11))

#szóljon ha kész a folyamat
for elem in range(11):
    print(elem, end=" ")
else:
    print("vége a folyamatnak!")

#szöveg kezelés
for elem in "szöveg szöbeg2":
    print(elem)

print("-"*50)
gyomolcslista = ["alma", "körte","banán", "kiwi", "narancs"]
for elem in gyomolcslista:
    print(elem)

print(f"A gyümölcsök listában {len(gyomolcslista)} db elem van")

#két for ciklus egymásba ágyazása!
tulajdonsagoklista = ["érett", "nagy", "édes"]
gyomolcslista2 = ["alma", "körte", "banán", "kiwi", "narancs"]

for i in tulajdonsagoklista:
    for j in gyomolcslista2:
        print(i,j)
