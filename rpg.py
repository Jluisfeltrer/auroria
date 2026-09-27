import random
import time
import os

# =========================
# ⚔️ LAS TIERRAS DE AURORIA
# =========================

def limpiar():
    os.system("clear" if os.name != "nt" else "cls")

def pausa():
    input("\nPulsa ENTER para continuar...")

def escribir(texto, velocidad=0.015):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()

# -------------------------
# PERSONAJE
# -------------------------

jugador = {
    "nombre": "",
    "nivel": 1,
    "xp": 0,
    "vida": 100,
    "vida_max": 100,
    "ataque": 12,
    "defensa": 5,
    "oro": 30,
    "pociones": 2,
    "arma": "Espada oxidada",
}

enemigos = [
    {"nombre": "Goblin", "vida": 35, "ataque": 8, "defensa": 2, "xp": 20, "oro": 10},
    {"nombre": "Lobo salvaje", "vida": 45, "ataque": 10, "defensa": 3, "xp": 25, "oro": 15},
    {"nombre": "Bandido", "vida": 55, "ataque": 13, "defensa": 5, "xp": 35, "oro": 25},
    {"nombre": "Orco", "vida": 75, "ataque": 17, "defensa": 7, "xp": 50, "oro": 40},
]

# -------------------------
# NIVEL
# -------------------------

def comprobar_nivel():
    necesario = jugador["nivel"] * 60

    if jugador["xp"] >= necesario:
        jugador["xp"] -= necesario
        jugador["nivel"] += 1
        jugador["vida_max"] += 20
        jugador["vida"] = jugador["vida_max"]
        jugador["ataque"] += 5
        jugador["defensa"] += 2

        print("\n✨ ======================== ✨")
        print("       ¡SUBES DE NIVEL!")
        print("✨ ======================== ✨")
        print(f"Ahora eres nivel {jugador['nivel']}.")
        print("+20 vida máxima")
        print("+5 ataque")
        print("+2 defensa")

# -------------------------
# ESTADÍSTICAS
# -------------------------

def mostrar_estado():
    print("\n╔══════════════════════════╗")
    print(f"║ ⚔️  {jugador['nombre']:<20} ║")
    print("╠══════════════════════════╣")
    print(f"║ Nivel:    {jugador['nivel']:<14} ║")
    print(f"║ ❤️ Vida:   {jugador['vida']}/{jugador['vida_max']:<7} ║")
    print(f"║ ⚔️ Ataque:  {jugador['ataque']:<12} ║")
    print(f"║ 🛡️ Defensa: {jugador['defensa']:<11} ║")
    print(f"║ ⭐ XP:      {jugador['xp']:<12} ║")
    print(f"║ 💰 Oro:     {jugador['oro']:<12} ║")
    print(f"║ 🧪 Pociones:{jugador['pociones']:<11} ║")
    print(f"║ 🗡️ Arma:    {jugador['arma']:<12} ║")
    print("╚══════════════════════════╝")

# -------------------------
# COMBATE
# -------------------------

def combate(enemigo):
    enemigo = enemigo.copy()

    escribir(f"\n⚔️ ¡Un {enemigo['nombre']} aparece ante ti!")

    while enemigo["vida"] > 0 and jugador["vida"] > 0:

        print("\n-------------------------")
        print(f"❤️ Tu vida: {jugador['vida']}/{jugador['vida_max']}")
        print(f"👹 {enemigo['nombre']}: {enemigo['vida']} HP")
        print("-------------------------")

        print("\n1. ⚔️ Atacar")
        print("2. 🧪 Usar poción")
        print("3. 🏃 Huir")

        opcion = input("\n¿Qué haces? ")

        if opcion == "1":

            daño = max(
                1,
                jugador["ataque"]
                + random.randint(-3, 5)
                - enemigo["defensa"]
            )

            # Golpe crítico
            if random.random() < 0.15:
                daño *= 2
                print("\n💥 ¡GOLPE CRÍTICO!")

            enemigo["vida"] -= daño
            print(f"\n⚔️ Has causado {daño} de daño.")

            if enemigo["vida"] <= 0:
                print(f"\n🏆 ¡Has derrotado al {enemigo['nombre']}!")
                jugador["xp"] += enemigo["xp"]
                jugador["oro"] += enemigo["oro"]

                print(f"⭐ +{enemigo['xp']} XP")
                print(f"💰 +{enemigo['oro']} oro")

                comprobar_nivel()
                return True

            # Ataque enemigo
            daño = max(
                1,
                enemigo["ataque"]
                + random.randint(-2, 4)
                - jugador["defensa"]
            )

            jugador["vida"] -= daño
            print(
                f"👹 {enemigo['nombre']} te golpea "
                f"y causa {daño} de daño."
            )

        elif opcion == "2":

            if jugador["pociones"] > 0:

                curacion = random.randint(25, 40)
                jugador["vida"] = min(
                    jugador["vida_max"],
                    jugador["vida"] + curacion
                )

                jugador["pociones"] -= 1

                print(f"\n🧪 Recuperas {curacion} puntos de vida.")

            else:
                print("\n❌ No tienes pociones.")

        elif opcion == "3":

            if random.random() < 0.5:
                print("\n🏃 ¡Has conseguido escapar!")
                return False
            else:
                print("\n❌ ¡No consigues escapar!")

        else:
            print("\n❓ Opción no válida.")

        if jugador["vida"] <= 0:
            print("\n💀 Has caído en combate...")
            return False

    return False

# -------------------------
# TIENDA
# -------------------------

def tienda():

    while True:
        print("\n🏪 ====================")
        print("        TIENDA")
        print("========================")

        print(f"\n💰 Tienes {jugador['oro']} de oro.")
        print("\n1. 🧪 Poción - 15 oro")
        print("2. 🗡️ Espada mejorada - 60 oro")
        print("3. 🛡️ Armadura - 80 oro")
        print("4. 🚪 Salir")

        opcion = input("\nComprar: ")

        if opcion == "1":

            if jugador["oro"] >= 15:
                jugador["oro"] -= 15
                jugador["pociones"] += 1
                print("🧪 Has comprado una poción.")
            else:
                print("❌ No tienes suficiente oro.")

        elif opcion == "2":

            if jugador["oro"] >= 60:

                jugador["oro"] -= 60
                jugador["ataque"] += 8
                jugador["arma"] = "Espada de acero"

                print("⚔️ ¡Tu ataque ha aumentado!")

            else:
                print("❌ No tienes suficiente oro.")

        elif opcion == "3":

            if jugador["oro"] >= 80:

                jugador["oro"] -= 80
                jugador["defensa"] += 6

                print("🛡️ ¡Tu defensa ha aumentado!")

            else:
                print("❌ No tienes suficiente oro.")

        elif opcion == "4":
            break

        else:
            print("❓ Opción no válida.")

# -------------------------
# EXPLORACIÓN
# -------------------------

def explorar():

    print("\n🌲 Te adentras en el bosque...")

    evento = random.randint(1, 5)

    if evento <= 3:

        enemigo = random.choice(enemigos)
        combate(enemigo)

    elif evento == 4:

        oro = random.randint(10, 35)
        jugador["oro"] += oro

        print(f"\n💰 ¡Encuentras una bolsa con {oro} monedas!")

    else:

        jugador["pociones"] += 1
        print("\n🧪 Encuentras una poción escondida.")

# -------------------------
# JEFE FINAL
# -------------------------

def jefe_final():

    limpiar()

    print("""
╔══════════════════════════════════╗
║                                  ║
║       🔥 EL DRAGÓN NEGRO 🔥      ║
║                                  ║
╚══════════════════════════════════╝
""")

    escribir(
        "Una criatura gigantesca desciende desde las montañas..."
    )

    dragon = {
        "nombre": "Dragón Negro",
        "vida": 180,
        "ataque": 25,
        "defensa": 10,
        "xp": 150,
        "oro": 200
    }

    return combate(dragon)

# -------------------------
# HISTORIA
# -------------------------

def aventura():

    limpiar()

    escribir(
        "\nHace cien años, el reino de Auroria fue protegido "
        "por una antigua espada legendaria."
    )

    escribir(
        "Pero una noche, el Dragón Negro despertó..."
    )

    escribir(
        "Ahora solo tú puedes encontrar la espada "
        "y enfrentarte a la criatura."
    )

    pausa()

    while jugador["nivel"] < 3:

        limpiar()

        print("🌎 ===========================")
        print("       MAPA DE AURORIA")
        print("==============================")

        print("\n1. 🌲 Explorar el bosque")
        print("2. 🏪 Visitar la tienda")
        print("3. 📜 Ver personaje")
        print("4. 🚪 Salir")

        opcion = input("\n¿Qué quieres hacer? ")

        if opcion == "1":
            explorar()
            pausa()

        elif opcion == "2":
            tienda()

        elif opcion == "3":
            mostrar_estado()
            pausa()

        elif opcion == "4":
            return

        else:
            print("❓ Opción no válida.")

        if jugador["vida"] <= 0:
            return

    # DECISIÓN FINAL

    limpiar()

    print("""
╔════════════════════════════════╗
║        🏰 EL CASTILLO          ║
╚════════════════════════════════╝
""")

    escribir(
        "Después de muchas batallas llegas al castillo."
    )

    escribir(
        "Frente a ti hay dos caminos."
    )

    print("\n1. ⚔️ Entrar por la puerta principal")
    print("2. 🥷 Entrar por un túnel secreto")

    opcion = input("\nTu decisión: ")

    if opcion == "2":
        print("\n🥷 Encuentras un cofre secreto.")
        jugador["oro"] += 100
        jugador["pociones"] += 2
        print("💰 +100 oro")
        print("🧪 +2 pociones")

    else:
        print("\n⚔️ Entras directamente al castillo.")

    pausa()

    jefe_final()

# -------------------------
# INICIO
# -------------------------

limpiar()

print("""
╔══════════════════════════════════════╗
║                                      ║
║       ⚔️  LAS TIERRAS DE AURORIA ⚔️  ║
║                                      ║
║             RPG TERMINAL             ║
║                                      ║
╚══════════════════════════════════════╝
""")

jugador["nombre"] = input("\n🧙 Introduce el nombre de tu héroe: ")

print(f"\nBienvenido, {jugador['nombre']}...")
time.sleep(1)

aventura()

print("\n\n🏆 FIN DE LA AVENTURA 🏆")
print("Gracias por jugar a Las Tierras de Auroria.")