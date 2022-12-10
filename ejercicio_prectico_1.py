"""
Conocido el número en matemática PI π, pedir al usuario que ingrese el valor del radio de
una circunferencia y calcular y mostrar por pantalla el área y perímetro. Recuerde que para
calcular el área y el perímetro se utilizan las siguientes fórmulas:
area = PI * radio2
perimetro = 2 * PI * radio
"""
give = int (input("Ingrese el valor de radio: "))

pi = 3.1416
area = pi * (give * give)
perimetro = 2 * pi * give

print(f"El area del redio es: {area} ")
print(f"El perimetro del redio es: {perimetro} ")
