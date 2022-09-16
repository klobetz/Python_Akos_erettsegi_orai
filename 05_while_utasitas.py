valasz = int(input("kérek egy számot: "))
# osszeg = 0
# db = 1
# while db <= valasz:
#     osszeg += db
#     db += 1
# print(osszeg)

print("-"*50)
osszeg2 = 0
for i in range(valasz+1):
    osszeg2 += i
    #print(i)
print(osszeg2)