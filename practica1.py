print("ingrese el % que desea calcular: ")
porcentaje = float(input())
print("ingrse el número base: ")
número = float(input())
resultado = porcentaje * número / 100
print("El ", número , "% de ", porcentaje, "es ", round(resultado, 3))