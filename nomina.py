empleados = [{
    "nombre":"Alexander",
    "cargo":"Administrador",
    "salario":2850000,
    "departamento":"ventas"
},
{
    "nombre":"Luis",
    "cargo":"Contador",
    "salario":3550000,
    "departamento":"contaduria"
},
{
     "nombre":"Carlos",
    "cargo":"Desarrollador",
    "salario":3890000,
    "departamento":"tecnologia"
}]

def mostrar_menu():
    print(f"\n{'=' * 40}")
    print("1. Registrar empleado")
    print("2. Ver todos los empleados")
    print("3. Nómina individual")
    print("4. Nómina completa")
    print("5. Buscar empleado")
    print("6. Eliminar empleado")
    print("7. Empleado mejor y peor pagado")
    print("8. Salir")
    print("=" * 40)

def registro_empleado():
    nombre = input("Nombre: ")
    cargo = input("Cargo: ")
    salario = int(input("Salario: "))
    departamento = input("Departamento: ")

    nuevo_empleado = {
        "nombre": nombre,
        "cargo" : cargo,
        "salario": salario,
        "departamento": departamento
        }
    empleados.append(nuevo_empleado)
    
    print(f"✔ {nombre} agregado correctamente")
    

def ver_empleados():
    if not empleados:
        print(f"❗ lista empleados vacia")
        return
    
    print(f"\n{'=' * 75}")
    print(f"{'NOMBRE':<20} {'CARGO':<12} {'SALARIO':<12} {'DEPARTAMENTO':<12}")
    print(f"{'=' * 75}")
    
    for empleado in empleados:
          print(f"{empleado['nombre']:<20} {empleado['cargo']:<12} ${empleado['salario']:<11,} {empleado['departamento']:<15}")
    
    print(f"{'=' * 75}")
    print(f"📊 Total: {len(empleados)} EMPLEADOS")









      
def nomina_empleado():
     nombre_empleado = input("Por favor ingrese el nombre del empleado a generar nomina: ")
     encontrado = False

     for empleado in empleados:
          
          if nombre_empleado.lower() == empleado["nombre"].lower():
               encontrado = True
               salario_base = empleado["salario"]
               cargo = empleado["cargo"]

               x_respuesta = ""
               while x_respuesta != "si" and x_respuesta != "no":
                   x_respuesta = input("El empleado tuvo horas EXTRA( SI / NO): ").lower()
                   if x_respuesta != "si" and x_respuesta != "no":
                       print("❗ respuesta ERRONEA. Escriba SI O NO ")
               if x_respuesta == "si":
                   horas_extras = float(input("Por favor ingrese el numero de horas EXTRA: "))
               else:
                   horas_extras = 0    
                   
               valor_horaextra = ((salario_base / 240) * 1.5) * horas_extras
               salud = salario_base * 0.04
               pension = salario_base * 0.04
               auxilio_trans = 117172
               neto = (salario_base + valor_horaextra + auxilio_trans) - (salud + pension)
               print(f"\n{'=' * 40}")
               print(f"{'NOMINA':^40}")
               print("=" * 40)
               print(f"Empleado     : {nombre_empleado}") 
               print(f"Cargo        : {cargo}")
               print(f"Salario base : ${salario_base:,.0f}")
               print(f"Horas extra  : ${valor_horaextra:,.0f}")
               print(f"Salud (4%)   : ${salud:,.0f}")
               print(f"Pension (4%) : ${pension:,.0f}")
               print(f"Auxilio trans: ${auxilio_trans:,.0f}")
               print("-" * 40)
               print(f"Neto a pagar : ${neto:,.0f}")
               return          
     if not encontrado:
         print("❗ Empleado no encontrado")




def nomina_completa():
    list_nomina = []
    
    for empleado in empleados:
        salario_base = empleado["salario"]
        nombre = empleado["nombre"]

        hora_extra = ""
        while hora_extra != "si" and hora_extra != "no":
            hora_extra = input(f"El empleado {nombre} realizo horas EXTRA(SI/ NO): ").lower()
            if hora_extra != "si" and hora_extra != "no":
                print("❗ RESPUESTA ERRONEA. ESCRIBA POR FAVOR SI O NO")
       
        if hora_extra == "si":
                total_horas = float(input("Por favor ingrese numero de horas EXTRA: "))
        else:
            total_horas = 0

        valor_hextras = ((salario_base / 240) * 1.5) * total_horas 
        pension = (salario_base + valor_hextras) * 0.04
        salud = (salario_base + valor_hextras) * 0.04
        deduccion = pension + salud
        auxilio = 117172
        neto = (salario_base + valor_hextras + auxilio) - deduccion
        
        resultado = {
             "nombre":empleado["nombre"],
             "cargo":empleado["cargo"],
             "salario_base":salario_base,
             "horas_extra":total_horas,
             "valor_hextra":valor_hextras,
             "salud":salud,
             "pension":pension,
             "auxilio":auxilio,
             "neto":neto

        }
        list_nomina.append(resultado)

    print("=" * 80)
    print("NOMINA COMPLETA DE LA EMPRESA". center(80))
    print("=" * 80)
    print(f"{'EMPLEADO':<20} {'SALARIO':>12} {'EXTRAS':>12}  {'DEDUCCIONES':>12} {'NETO':>12}")
    print("-" * 80)

    total_empresa = 0
    for empl in list_nomina:
         deducciones = empl["salud"] + empl["pension"]
         print(F"{empl['nombre']:<20} ${empl['salario_base']:>11,.1f} ${empl['valor_hextra']:>11,.1f} ${deducciones:>11,.1f} ${empl['neto']:>11,.1f}")
         total_empresa += empl["neto"]
    print("-" * 80)
    print(f"{'TOTAL NOMINA EMPRESA':<56} ${total_empresa:>15,.1f}")
    print("=" * 80)

         
def buscar_empleado():
     buscar = input("Favor ingrese el nombre del empleado a buscar: ") 
     encontrado = False
     for empleado in empleados:
          if buscar.lower() == empleado["nombre"].lower():
               print("=" * 40)
               print(f"\n ✔ EMPLEADO ENCONTRADO")
               print("=" * 40)
               print(f"NOMBRE        :  {empleado['nombre']}")
               print(f"CARGO         :  {empleado['cargo']}")
               print(f"SALARIO       :  {empleado['salario']}")
               print(f"DEPARTAMENTO  :  {empleado['departamento']}")
               print("=" * 40)
               encontrado = True
               break
     if not encontrado:
          print(f"NO SE ENCONTRO '{buscar}' ") 
     return     
           
def eliminar_empleado():
    empleado_eliminar = input("Ingrese nombre del empleado a elimnar: ")
    for empleado in empleados:
        if empleado_eliminar.lower() == empleado["nombre"].lower():
            empleados.remove(empleado)
            print(f"✔ {empleado_eliminar} Eliminado de inventario")
            return
    print(f"❗ Producto '{empleado_eliminar}' no encontrado") 
   
     
def empleado_maxmin():
     if not empleados:
          print("📄 lista vacia ")
          return
     empleado_max = empleados[0]
     empleado_min = empleados[0]
     for empl in empleados:
          if empl["salario"] > empleado_max["salario"]:
               empleado_max = empl
          if empl["salario"] < empleado_min["salario"]:
               empleado_min = empl
     print(f"\n💰 El empleado mejor pagado es : {empleado_max['nombre']} - ${empleado_max['salario']:,.0f}")
     print(f"💸 El empleado con salario mas bajo es : {empleado_min['nombre']} - ${empleado_min['salario']:,.0f}")          


while True:
    mostrar_menu()
    opcion = input("\n→ Elige una opción: ")

    if opcion == "1":
        registro_empleado()
    elif opcion == "2":
        ver_empleados()
    elif opcion == "3":
        nomina_empleado()
    elif opcion == "4":
        nomina_completa()
    elif opcion == "5":
        buscar_empleado()
    elif opcion == "6":
        eliminar_empleado()
    elif opcion == "7":
        empleado_maxmin()
    elif opcion == "8":
        print("👋 Hasta luego!")
        break
    else:
        print("❗ Opción inválida")





                            
                       

            
                  
               

               



             
               






     
                
              
          
          
          
     
  

    