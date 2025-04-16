import random

Num1 = int(input("ingrese un número "))
Num2 = random.randint(0, 1000)

Num1 = int(Num1)
Num2 = int(Num2)

while Num1 == Num2:
    Num2 = random.randint(0, 1000)
print("Este número es: ", Num2)

if Num1 > Num2:
    print("Este número ingresado por el usuario es mayor al segundo ")

elif Num1 < Num2:
    print("Este número ingresado por el usuario es menor que el segundo ")

else:
    print("Ambos números son = ")