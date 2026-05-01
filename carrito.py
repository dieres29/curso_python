catalogo = [
    # Electrónica
    {"id": 1, "nombre": "Televisor Samsung 43\"", "precio": 1250000, "categoria": "electronica", "stock": 5},
    {"id": 2, "nombre": "Celular Infinix", "precio": 850000, "categoria": "electronica", "stock": 8},
    {"id": 3, "nombre": "Laptop Lenovo", "precio": 2800000, "categoria": "electronica", "stock": 3},
    
    # Ropa
    {"id": 4, "nombre": "Camiseta Deportiva", "precio": 45000, "categoria": "ropa", "stock": 20},
    {"id": 5, "nombre": "Pantalón Jeans", "precio": 89000, "categoria": "ropa", "stock": 15},
    {"id": 6, "nombre": "Chaqueta Cuero", "precio": 180000, "categoria": "ropa", "stock": 5},
    
    # Hogar
    {"id": 7, "nombre": "Sartén Antiadherente", "precio": 65000, "categoria": "hogar", "stock": 12},
    {"id": 8, "nombre": "Lámpara LED", "precio": 45000, "categoria": "hogar", "stock": 10}
]


carrito = []

historial = []


# Lista de administradores
administradores = [
    {"usuario": "Alexander", "contrasena": "alex123"},
    {"usuario": "Luis", "contrasena": "luis456"},
    {"usuario": "Carlos", "contrasena": "carlos789"}
]

# Categorías válidas (global)
CATEGORIAS_VALIDAS = ["electronica", "ropa", "hogar"]

#funciones compartidas
def mostrar_menu_inicio():

    print(f"\n{'=' * 40}")
    print("BIENVENIDO A APPFINDER STORE".center(40))
    print("=" * 40)
    print("1️⃣  Soy Administrador ")
    print("2️⃣  Soy Cliente")
    print("3️⃣  Salir")
    print("=" * 40)

#funciones admin
def verficiar_contraseña():
    usuario = input("por favor ingrese NOMBRE DE USUARIO: ")
    contrasena = input("ingresar CONTRASEÑA POR FAVOR ")
    
    for admin in administradores:
        if admin["usuario"] == usuario and admin["contrasena"] == contrasena:
            print(f"\n ✔✔ BIENVENIDO {usuario}")
            mostar_menu_admin()
            return
        
    print("\n ❗❗ USUARIO O CONTRASEÑA INCORRECTOS")  
    input("presione ENTER para continuar..")  



def mostrar_menu_admin():
    while True:
        print(f"\n{'=' * 40}")
        print("MENÚ ADMINISTRADOR".center(40))
        print("=" * 40)
        print("1️⃣  Ver catálogo")
        print("2️⃣  Agregar producto")
        print("3️⃣  Eliminar producto")
        print("4️⃣  Ver historial de ventas")
        print("5️⃣  Volver al menú principal")
        print("=" * 40)
        
        opcion = input("\n→ Elige una opción: ")
        
        if opcion == "1":
            ver_catalogo()
        elif opcion == "2":
            agregar_producto_catalogo()
        elif opcion == "3":
            eliminar_producto_catalogo()
        elif opcion == "4":
            ver_historial_admin()
        elif opcion == "5":
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("❗ Opción inválida")


def agregar_producto_catalogo():

    id_producto = len(catalogo) + 1
    nombre = input("nombre Producto: ")
    precio = int(input("precio: "))
   
    print(f"\n 📍 CATEGORIAS DISPONIBLES: {',|'.join(CATEGORIAS_VALIDAS)}")
    while True:
        categoria = input("CATEGORIA: ").lower()
        if categoria in CATEGORIAS_VALIDAS:
            break
        else:
            print(f"❗❗ CATEGORIA INVALIDA . ELIJE ENTRE: {',|'.join(CATEGORIAS_VALIDAS) }")
    stock = int(input("stock: "))

    nuevo_producto= {
        "id": id_producto,
        "nombre": nombre,
        "precio" : precio,
        
        "categoria": categoria,
        "stock": stock
        }
    catalogo.append(nuevo_producto)
    
    print(f"✔ {nombre} agregado correctamente")


def eliminar_producto_catalogo():
    print("\n 📈 CATALOGO ACTUAL")
    for producto in catalogo:
        print(f"   id {producto ['id']} - {producto ['nombre']} - (STOCK{producto ['stock']}) ")
        print("-" * 40)


    while True:  
        producto_eliminar = int(input("INGRESE EL ID DEL PRODCUTO A ELIMINAR: "))
        if producto_eliminar == 0:
            print("OPERACION CANCELADA")
            return
        for producto in catalogo:
            if producto_eliminar == producto["id"]:
                catalogo.remove(producto)
                print(F"PRODUCTO ID {producto_eliminar}  ELIMINADO DEL CATALOGO")
                return
        print(f"PRODUCTO A ELIMINAR CON ID {producto_eliminar} NO ENCONTRADO . INTENTE DE NUEVO")    
 
def ver_catalogo():
    if not catalogo:
        print("📦  EL CATALOGO ESTA VACIO 📦")
        return
    nombres_categorias = {
        "electronica": "📱 ELECTRONICA",
        "ropa": "👔 ROPA",
        "hogar": "🏠 HOGAR"
    }

    for categoria in CATEGORIAS_VALIDAS:
        print(f"\n{'=' * 55}")
        print(nombres_categorias[categoria].center(55))
        print("=" * 55)
        print(f"{'ID':<5} {'NOMBRE':<30} {'PRECIO':>12} {'STOCK':>6}")
        print("-" * 55)


        encontrados = 0
        for producto in catalogo:
            if producto["categoria"] == categoria:
                encontrados += 1
                print(f"{producto['id']:<5} {producto['nombre']:<30} ${producto['precio']:>11,} {producto['stock']:>6}")
        
        if encontrados == 0:
            print("   (No hay productos en esta categoría)")
    
    print(f"\n{'=' * 55}")
    print(f"📊 Total de productos: {len(catalogo)}".center(55))
    print("=" * 55)


  
    
 