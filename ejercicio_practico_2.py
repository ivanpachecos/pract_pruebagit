"""
Escribir un programa que calcule el precio promedio de un producto. El precio promedio se
debe calcular a partir del precio del mismo producto en tres establecimientos distintos.
"""
prodcto_ingresado = float (input("Ingrese el valor del producto: "))

prodcto_ingresado = (prodcto_ingresado + prodcto_ingresado + prodcto_ingresado)/3

print("El precio promedio  es: ", int(prodcto_ingresado))

