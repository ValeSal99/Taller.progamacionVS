# -*- coding: utf-8 -*-
"""Taller de repaso 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nOu7r4WUFJLrL0kbJcqJ1NfvhvCalj9-
"""

#Punto 2 del taller
# variable para capturar la venta
venta = float(input("¿Cuánto fue el total de la compra? "))
# cálculo del desucento 
descuento = venta * 0.15
# Resta del descuento con la venta
total = venta - descuento
# Visualiza el total a pagar por pantalla
print("El descuento es = {:,.0f} y el total a pagar es = {:,.0f}".format(descuento, total))
print(f"El descuento es = {descuento:,.0f} y el total a pagar es = {total:,.0f}")

#Punto 3 del taller
cal1 = float(input("Digite la calificaicón 1: "))
cal2 = float(input("Digite la calificaicón 2: "))
cal3 = float(input("Digite la calificaicón 3: "))

prom = round((cal1 + cal2 + cal3 ) /3, 2)

print(f"El promedio es= {prom}")

#Punto 4 del taller
Total_estudiantes = input("Total estudiantes: ")
NumH = input("Numero de hombres: ")
NumM = input("Numero de mujeres: ")
Porcentaje1 = int(NumH) * 100/ int(Total_estudiantes)
Porcentaje2 =int(NumM) * 100/ int(Total_estudiantes)
print(f"el porcetaje de hombres es: {Porcentaje1} y el porcentaje de mujeres es {Porcentaje2}")