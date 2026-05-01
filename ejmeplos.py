"""Ejercicio 6 — Reto 🔥
Construye un sistema de facturación de AppFinder usando funciones:
calcular_subtotal(precio, cantidad)   → precio × cantidad
calcular_iva(subtotal)                → subtotal × 19%
calcular_total(subtotal, iva)         → subtotal + iva
mostrar_factura(producto, precio, cantidad, tienda)  → usa todas las anteriores
La factura debe verse así:
========================================
        FACTURA APPFINDER
========================================
  Producto  : Televisor Samsung
  Tienda    : Falabella
  Precio    : $1,250,000
  Cantidad  : 2
  Subtotal  : $2,500,000
  IVA 19%   : $475,000
----------------------------------------
  TOTAL     : $2,975,000"""

def calcular_subtotal(precio, cantidad):

    subtotal = precio * cantidad 
    return subtotal

def calcular_iva(subtotal):
    iva = subtotal * 0.19
    return iva

def calcular_total(subtotal, iva):
     total = subtotal + iva
     return total

def mostrar_factura(nombre, tienda, precio, cantidad ):
    subtotal = calcular_subtotal(precio, cantidad)
    iva = calcular_iva(subtotal)
    total = calcular_total(subtotal, iva)
    print(f"\n{'=' * 40}")
    print(f"  FACTURA APPFINDER")
    print(f"{'=' * 40}")
    print(f"PRODUCTO : {nombre}")
    print(f"TIENDA   : {tienda}")
    print(f"PRECIO   : ${precio :,} ")
    print(f"CANTIDAD : {cantidad}")
    print(f"SUBTOTAL :{subtotal: ,}")
    print(f"IVA 19%  :{iva: ,}")
    print("-" * 40)
    print(f"TOTAL    :{total: ,}")


precio = int(input("ingrese precio del producto: $ "))
nombre = input("ingrese nombre producto: ")
cantidad = int(input("ingrese cantidad de articulos: # "))
tienda = input("ingrese tienda: ")
mostrar_factura(nombre, tienda, precio, cantidad )



x_respuesta = ""
while x_respuesta != "si" and x_respuesta != "no":
    x_respuesta = input("El empleado tuvo horas extras(SI/NO): ").lower()
    if x_respuesta != "si" and x_respuesta != "no":
        print("❗ respuesta ERRONEA. Escriba SI O NO ")

if x_respuesta == "si":
    horas_extras = float(input("Ingrese numero de horas extras:"))
else:
    horas_extras = 0
print(horas_extras)    
   


    





    
    



    


    