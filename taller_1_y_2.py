# -*- coding: utf-8 -*-
"""Taller 1 y 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fICOiASkvorhrmP48bC2qHKoUZxWoFqX
"""

Numero_identificacion = input("Número de identificación: ")
print(Numero_identificacion)

NombreP = input("Nombre/s: ")
print(NombreP)

ApellidoP = input("Apellidos: ")
print(ApellidoP)

DireccionP = input( "Direccion: ")
print(DireccionP)

TelefonoP = input("Teléfono: ")
print(TelefonoP)

EdadP = int(input("Edad: "))
print(EdadP)
if EdadP > 55:
  print("Usted disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico")
elif EdadP < 55:
  print("No disfruta de bono")

Estado_civil = input("Estado Civil: ")
print(Estado_civil)
if Estado_civil == 'Casado' or Estado_civil == 'Casada':
  print("Obtiene un paseo cada diciembre")
elif Estado_civil == 'Soltero' or Estado_civil == 'Soltera':
  print("No obtiene paseo")
else:
  print("La palabra ingresada no forma parte de lo preguntado")

Numero_hijos = int(input("Numero de Hijos: "))
print(Numero_hijos)
if Numero_hijos > 0:
  print("Obtiene un paseo cada diciembre")
elif Numero_hijos == 0:
  print(" No Obtiene un paseo cada diciembre")

EstaturaCm = input("Estatura en cm: ")
print(EstaturaCm)

Fecha_de_contratación = input("Fecha de contratación: ")
print(Fecha_de_contratación)

Sueldo_Basico = int(input("Sueldo básico: "))
print(Sueldo_Basico)
if 1000000<Sueldo_Basico and Sueldo_Basico<1500000:
  Comision = Sueldo_Basico*0.2
  Total = Comision + Sueldo_Basico
  print(f"Comision de 2% del sueldo basico sería : {Comision:,.0f}")
  print(f"El sueldo total sería : {Total:,.0f}")
elif 1500001<Sueldo_Basico and Sueldo_Basico<2000000:
  Comision = Sueldo_Basico*0.5
  Total = Comision + Sueldo_Basico
  print(f"Comision de 5% del sueldo basico sería : {Comision:,.0f}")
  print(f"El sueldo total sería : {Total:,.0f}")
else:
  print("No aplica comisión")

try:
  Dias_Laborados = int(input("Días Laborados: "))
  print(Dias_Laborados)
  if Dias_Laborados>20:
    print("Recibe bono de alimentación")
  elif Dias_Laborados<20:
    print("No aplica bono de alimentación")
except:
  print("caracter no valido")