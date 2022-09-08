lista = [5, 47, 8, 54, 6, 2, 15, 4, 1, 25, 10, 65, 17, 321]

#írassuk ki a 20 nál kisebb számokat
for elem in lista:
    if elem <= 20:
        print(elem, end=", ")

#írasuk ki a lista elemeit ameddig nem találom meg a 10-et
print()
for elem in lista:
    if elem == 10:
        break
    print(elem, end=", ")

print("\nok")

