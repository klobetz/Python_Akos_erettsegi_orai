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
