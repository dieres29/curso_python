import random
<<<<<<< HEAD
ranking = []
=======
>>>>>>> 6b256d539c3f59992890a1c2d64694d673d3a5a3

def menu():
    print(f"\n{'=' * 40}")
    print("MENU JUEGO".center(40))
    print("=" * 40)
    print("1️⃣  Jugar")
    print("2️⃣  Ver ranking de jugadores")
    print("3️⃣  Ver instrucciones")
    print("4️⃣  Salir")
    print("=" * 40)


def mostrar_instrucciones():
    print(f"\n{'=' * 45}")
    print("INSTRUCCIONES".center(45))
    print("=" * 45)
    print("""
  🎯 OBJETIVO:
  Adivina el número secreto generado
  por el computador.

  📊 NIVELES:
  1. Fácil   → número entre 1 y 50
               máximo 10 intentos
  2. Medio   → número entre 1 y 100
               máximo 7 intentos
  3. Difícil → número entre 1 y 200
               máximo 5 intentos

  🌡️  PISTAS:
  Muy frío    → diferencia > 50
  Frío        → diferencia > 20
  Tibio       → diferencia > 10
  Caliente    → diferencia > 5
  Muy caliente→ diferencia <= 5

  🏆 PUNTAJE:
  Intento 1 → 100 puntos
  Intento 2 →  90 puntos
  Intento 3 →  80 puntos
  ...resta 10 por cada intento
    """)
    print("=" * 45)


def elegir_nivel():
    while True:
        try:
            nivel = int(input("Elige nivel (1, 2, 3): "))
            if nivel == 1:
                print("Elegiste Fácil — números 1-50, 10 intentos")
                return 1, 50, 10
            elif nivel == 2:
                print("Elegiste Medio — números 1-100, 7 intentos")
                return 2, 100, 7
            elif nivel == 3:
                print("Elegiste Difícil — números 1-200, 5 intentos")
                return 3, 200, 5
            else:
                print("❗ Elige 1, 2 o 3")
        except ValueError:
            print("❗ Debes ingresar un número válido (1, 2 o 3)")


def dar_pista(secreto, intento):
    diferencia = abs(secreto - intento)
    
    if diferencia > 50:
        return "🥶 Muy frío"
    elif diferencia > 20:
        return "❄️  Frío"
    elif diferencia > 10:
        return "🌡️  Tibio"
    elif diferencia > 5:
        return "🔥 Caliente"
    else:
        return "🌋 Muy caliente"
    
def calcular_puntaje(intentos_usados, nivel):
    puntaje_base = 100 - ((intentos_usados - 1) * 10)
    if puntaje_base < 10:
        puntaje_base = 10

    if nivel == 1:
        multiplicador = 1.0
    elif nivel == 2:
        multiplicador = 1.5
    else:
        multiplicador = 2.0

    puntaje_final = puntaje_base * multiplicador
    return int(puntaje_final)            
   
def jugar():

    nivel, limite, intentos_max = elegir_nivel()
    numero_secreto = random.randint(1, limite)
    intentos_usados = 0
<<<<<<< HEAD
    adivinado = False
=======
    adivindo = False
>>>>>>> 6b256d539c3f59992890a1c2d64694d673d3a5a3

    print(f"\n🔢 Adivina el número entre 1 y {limite}")
    print(f"💪 Tienes {intentos_max} intentos")
    print("-" * 40)


<<<<<<< HEAD
    while intentos_usados < intentos_max and not adivinado:
        intento = int(input("por favor ingrese numero: "))
        intentos_usados += 1
        if intento == numero_secreto:
            adivinado = True
            print(f"🎉🎉 ¡ felicitaciones ! Adivinaste en {intentos_usados} intentos")
        else:
            pista = dar_pista(numero_secreto, intento)
            print(f"no es {intento} . {pista}")
            print(f"Te quedan {intentos_max - intentos_usados}")

    if adivinado:
        puntaje = calcular_puntaje(intentos_usados, nivel)
        print(f"🏆🏆 tu puntaje : {puntaje} puntos") 
        nombre = input("Ingrese su nombre para el ranking: ")  
        nuevo_registro = {
            "nombre" : nombre,
            "puntaje" : puntaje,
            "nivel" : nivel,
            "intentos" : intentos_usados 
        }

        ranking.append(nuevo_registro)
        print("✔✔ Puntaje guardado en el ranking")

    else:
        print(f"\n 😖😖 Agotaste tus intentos ¡¡ . El numero era {numero_secreto}") 

def ver_ranking():

    if not ranking: 
        print("❗ No hay puntajes guardados ❗")
        print("JUEGA UNA PARTIDA PARA APARECER EN EL RANKING")
        return  # ← La función termina aquí si no hay ranking
    
    # Si llegamos aquí, es porque SÍ hay ranking
    ranking_ordenado = []
    ranking_temp = ranking.copy()
    
    while ranking_temp:
        mayor = ranking_temp[0]
        for jugador in ranking_temp:
            if jugador["puntaje"] > mayor["puntaje"]:
                mayor = jugador
        ranking_ordenado.append(mayor)
        ranking_temp.remove(mayor)
    
    # Mostrar ranking
    print("\n" + "=" * 55)
    print("🏆 RANKING DE JUGADORES 🏆".center(55))
    print("=" * 55)
    print(f"{'#':<4} {'NOMBRE':<20} {'PUNTAJE':>8} {'NIVEL':>10} {'INTENTOS':>8}")
    print("-" * 55)
    
    posicion = 1
    for jugador in ranking_ordenado[:10]:
        if jugador["nivel"] == 1:
            nivel_texto = "Fácil"
        elif jugador["nivel"] == 2:
            nivel_texto = "Medio"
        else:
            nivel_texto = "Difícil"
        
        print(f"{posicion:<4} {jugador['nombre']:<20} {jugador['puntaje']:>8} {nivel_texto:>10} {jugador['intentos']:>8}")
        posicion += 1
    
    print("=" * 55)
    print(f"📊 Total de jugadores: {len(ranking)}")

    
while True:
    menu()
    opcion = input("\n→ Elige una opción: ")

    if opcion == "1":
        jugar()
    elif opcion == "2":
        ver_ranking()
    elif opcion == "3":
        mostrar_instrucciones()
    
        
    elif opcion == "4":
        print("👋 Hasta luego!")
        break
    else:
        print("❗ Opción inválida")
    
       



           

            


=======
>>>>>>> 6b256d539c3f59992890a1c2d64694d673d3a5a3

     





