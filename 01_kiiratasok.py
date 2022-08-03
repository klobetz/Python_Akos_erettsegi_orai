#képernyőre kiíratás
print("Első programom!")            #futtatáshoz shift+ctrl+F10
print('Első programom!')            #vagy így
print('Első programom! "idézet" ')
#print("Első programom! "idézet" ")            #ez íg hibás kiíratás SyntaxError:

#több sorbn való kiíratás?
print('második '                 #ez így egy sorban írja ki a kiíratást
      'programom! de nem jó')
#ezt használjuk több sorhoz!
print("""első sor
valami
valami kettő
""")

#típusok
a = 0
print(a)
a = 15                  #int típus (szám)
print(type(a))
print(a)