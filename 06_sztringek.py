#egységben kezelt sztringek
sztring = "Járványhelyzet"
print(sztring)
print(sztring.upper())
print(sztring.lower())
print(sztring.swapcase())

#print(sztring[19]) #adott karakter
print(sztring[1]) #adott karakter
print(len(sztring))
print(sztring[-1])

for elem in sztring:
    print(elem,end="")

print("*"*50)
print()

i = 0
while i < len(sztring):
    print(sztring[i])
    i+=1

#szeletelés
print(sztring[2:5])
print(sztring[:5])
print(sztring[5:])
print(sztring[:5])
print(sztring[7:])

#karakterek vizsgálata in és a not operátorok:
# in operátor:
print("a" in sztring)

if "a" in sztring:
    print("szerepel")
else:
    print("nem szerepel")

#not opreátor:
print("a" not in sztring)
if "a" not in sztring:
    print("nem szerepel")
else:
    print("szerepel")

#beépített find metodus

varos = "Körmend"

print(varos.find("ö"))
print(type(varos.find("ö")))
print(f"A keresett karakter a/az {varos.find('ö')+1} helyen szerepel.")
#ha nincs benne akkor (-1)
print(varos.find("á"))

mandat = "Én már kezdem érteni az adott tananyagot!"
print(mandat.split())
lista = mandat.split()
print(type(lista))

for elem in lista:
    print(elem, end=" ")

print()
print(len(mandat.split()))

