# Punto 2 del taller 1:
# Realice un programa que lea 
# tres números reales y determine cuál es el mayor.
a=float
b=float
c=float
a = input("digite un primer numero : ")
b = input("digite otro numero : ")
c = input("digite un ultimo numero : ")
if a>b and a>c :
    print(a, " es el numero mayor.")
elif b>a and b>c :
    print(b, " es el numero mayor.")
elif c>a and c>b :
    print( c, " es el numero mayor.")