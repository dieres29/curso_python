inventario = [{
    "nombre":"celular Infinix",
    "precio":850000,
    "tienda":"Exito",
    "categoria":"electronica",
    "stock":8,
},
{
    "nombre":"pantalon",
    "precio":99000,
    "tienda":"koaj",
    "categoria":"ropa",
    "stock":15,
},
{
    "nombre":"cortina",
    "precio":155000,
    "tienda":"falabella",
    "categoria":"hogar",
    "stock":40,
}]

# 2️⃣ SEGUNDO — defines todas las funciones
def mostrar_menu():
    
    print(f"\n{'=' * 40}")
    print("1. Agregar producto")
    print("2. Ver todos los productos")
    print("3. Buscar por nombre")
    print("4. Actualizar precio")
    print("5. Eliminar producto")
    print("6. Ver por categoría")
    print("7. Producto más barato y más caro")
    print("8. Salir")
    print("=" * 40)
    

def agregar_producto():
    nombre = input("nombre: ")
    precio = int(input("precio: "))
    tienda = input("tienda: ")
    categoria = input("categoria: ")
    stock = int(input ("stock: "))

    nuevo_producto = {
        "nombre":nombre,
        "precio":precio,
        "tienda":tienda,
        "categoria":categoria,
        "stock":stock

    }
    inventario.append(nuevo_producto)
    print(f"✅ {nombre} agregado correctamente")
   

    

def mostrar_productos():
    if not inventario:
        print("📦 El inventario esta vacio")
        return
    print(f"\n{'=' * 75}")
    print(f"{'PRODUCTO':<20} {'PRECIO':>12} {'TIENDA':<12} {'CATEGORÍA':<12} {'STOCK':>6}")
    print(f"{'=' * 75}")
    
    for producto in inventario:
        print(f"{producto['nombre']:<20} ${producto['precio']:>11,} {producto['tienda']:<12} {producto['categoria']:<12} {producto['stock']:>6}")
    
    print(f"{'=' * 75}")
    print(f"📊 Total: {len(inventario)} productos")
    
    

def buscar_por_nombre():
    buscar = input("buscar por nombre: ")
    encontrado = False
    for producto in inventario:
        if buscar.lower() == producto["nombre"].lower():
             print(f"\n✅ Producto encontrado:")
             print(f"  Nombre    : {producto['nombre']}")
             print(f"  Precio    : ${producto['precio']:,.0f}")
             print(f"  Tienda    : {producto['tienda']}")
             print(f"  Categoría : {producto['categoria']}")
             print(f"  Stock     : {producto['stock']}")
             encontrado = True
             break
 
    if not encontrado:
        print(f"❗ no se encontro: '{buscar}' ")        
    
    return  
        
    

def actualizar_precio():
    nombre_producto = input("ingrese nombre producto a actualizar: ")
    nuevo_precio = int(input("ingrese nuevo precio: "))

    for producto in inventario:
        if nombre_producto.lower() == producto["nombre"].lower():
            producto["precio"] = nuevo_precio
            print(f"✔ Precio actualizado: {producto['nombre']} ➡ ${nuevo_precio:,.0f}")
            return
    print(f"❗ Producto '{nombre_producto}' no encontrado")    

    

def eliminar_producto():
    producto_eliminar = input("Ingrese nombre del producto a elimnar: ")
    for producto in inventario:
        if producto_eliminar.lower() == producto["nombre"].lower():
            inventario.remove(producto)
            print(f"✔ {producto_eliminar} Eliminado de inventario")
            return
    print(f"❗ Producto '{producto_eliminar}' no encontrado")    
    

def ver_por_categoria():
    categoria = input("Ingrese categoria a buscar: ")
    encontrado = False

    print(f"\n{'=' * 50}")
    print(f"📂 Categoría: {categoria.upper()}")
    print(f"{'=' * 50}")

    for producto in inventario:
        if categoria.lower() == producto["categoria"].lower():
            print(f"\n {'=' * 40}") 
            print(f"La categoria elegia es: {producto['categoria']}")
            print(f"Nombre producto: {producto["nombre"]}")
            print(f"Precio producto: {producto["precio"]:,.0f}")
            print(f"Tienda producto: {producto["tienda"]}")
            print(f"Stock producto: {producto["stock"]} unidades ")
            print("=" * 40)
            encontrado = True
        if not encontrado:
            print(f"\n❗ Categoría '{categoria}' no encontrada")   
        else:
            print(f"\n{'=' * 50}")

            

    
    
def producto_min_max():
    if not inventario:
        print("📦 Inventario vacío")
        return
    
    producto_costoso = inventario[0]
    producto_barato = inventario[0]
    
    for producto in inventario:
        if producto["precio"] > producto_costoso["precio"]:
            producto_costoso = producto
        if producto["precio"] < producto_barato["precio"]:
            producto_barato = producto
    
    # Estos print van FUERA del for
    print(f"\n💰 Más caro: {producto_costoso['nombre']} - ${producto_costoso['precio']:,.0f}")
    print(f"💸 Más barato: {producto_barato['nombre']} - ${producto_barato['precio']:,.0f}")

    


while True:
    mostrar_menu()
    opcion = input("\n→ Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_por_nombre()
    elif opcion == "4":
        actualizar_precio()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        ver_por_categoria()
    elif opcion == "7":
        producto_min_max()
    elif opcion == "8":
        print("👋 Hasta luego!")
        break
    else:
        print("❗ Opción inválida")







