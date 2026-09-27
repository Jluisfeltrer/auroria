import random


class Juego:

    def __init__(self, nombre="Héroe", avatar="🧙‍♂️"):

        self.jugador = {
            "nombre": nombre,
            "avatar": avatar,

            "nivel": 1,
            "xp": 0,

            "vida": 100,
            "vida_max": 100,

            "ataque": 12,
            "defensa": 5,

            "oro": 30,

            "pociones": 2,
            "arma": "Espada oxidada",

            # Estadísticas acumuladas
            "enemigos_derrotados": 0,
            "oro_conseguido": 0,
            "daño_causado": 0,
            "daño_recibido": 0,
        }

        self.enemigo = None

        self.tienda_abierta = False


    # ========================================================
    # ESTADO COMPLETO
    # ========================================================

    def estado(self):

        return {
            "jugador": self.jugador,
            "enemigo": self.enemigo,
            "tienda_abierta": self.tienda_abierta
        }


    # ========================================================
    # CAMBIAR PERSONAJE
    # ========================================================

    def configurar_personaje(self, nombre, avatar):

        if not nombre.strip():

            nombre = "Héroe"

        self.jugador["nombre"] = nombre.strip()
        self.jugador["avatar"] = avatar

        return self.estado()


    # ========================================================
    # EXPLORAR
    # ========================================================

    def explorar(self):

        if self.enemigo is not None:

            return {
                "tipo": "combate",
                "mensaje": (
                    "⚔️ ¡Estás en combate! "
                    "Debes luchar o huir."
                ),
                "estado": self.estado()
            }


        if self.tienda_abierta:

            return {
                "tipo": "tienda",
                "mensaje": (
                    "🏪 Primero debes salir de la tienda."
                ),
                "estado": self.estado()
            }


        evento = random.randint(1, 5)


        # ----------------------------------------------------
        # ENEMIGO
        # ----------------------------------------------------

        if evento <= 3:

            enemigos = [

                {
                    "nombre": "Goblin",
                    "vida": 35,
                    "vida_max": 35,
                    "ataque": 8,
                    "defensa": 2,
                    "xp": 20,
                    "oro": 10,
                },

                {
                    "nombre": "Lobo salvaje",
                    "vida": 45,
                    "vida_max": 45,
                    "ataque": 10,
                    "defensa": 3,
                    "xp": 25,
                    "oro": 15,
                },

                {
                    "nombre": "Bandido",
                    "vida": 55,
                    "vida_max": 55,
                    "ataque": 13,
                    "defensa": 5,
                    "xp": 35,
                    "oro": 25,
                },

                {
                    "nombre": "Orco",
                    "vida": 75,
                    "vida_max": 75,
                    "ataque": 17,
                    "defensa": 7,
                    "xp": 50,
                    "oro": 40,
                }
            ]

            self.enemigo = random.choice(enemigos).copy()

            return {
                "tipo": "combate",

                "mensaje": (
                    f"👹 ¡Un {self.enemigo['nombre']} "
                    "aparece entre los árboles!"
                ),

                "estado": self.estado()
            }


        # ----------------------------------------------------
        # ORO
        # ----------------------------------------------------

        elif evento == 4:

            oro = random.randint(10, 35)

            self.jugador["oro"] += oro
            self.jugador["oro_conseguido"] += oro

            return {
                "tipo": "oro",

                "mensaje": (
                    f"💰 ¡Has encontrado {oro} "
                    "monedas de oro!"
                ),

                "estado": self.estado()
            }


        # ----------------------------------------------------
        # POCIÓN
        # ----------------------------------------------------

        else:

            self.jugador["pociones"] += 1

            return {
                "tipo": "pocion",

                "mensaje": (
                    "🧪 ¡Has encontrado una poción!"
                ),

                "estado": self.estado()
            }


    # ========================================================
    # ATACAR
    # ========================================================

    def atacar(self):

        if self.enemigo is None:

            return {
                "mensaje": "No hay ningún enemigo.",
                "estado": self.estado()
            }


        dano = max(
            1,
            self.jugador["ataque"]
            + random.randint(-3, 5)
            - self.enemigo["defensa"]
        )


        critico = random.random() < 0.15


        if critico:

            dano *= 2

            mensaje = (
                f"💥 ¡GOLPE CRÍTICO!\n"
                f"⚔️ Has causado {dano} "
                "puntos de daño."
            )

        else:

            mensaje = (
                f"⚔️ Has causado {dano} "
                "puntos de daño."
            )


        self.enemigo["vida"] -= dano

        self.jugador["daño_causado"] += dano


        # ----------------------------------------------------
        # ENEMIGO DERROTADO
        # ----------------------------------------------------

        if self.enemigo["vida"] <= 0:

            nombre = self.enemigo["nombre"]

            xp = self.enemigo["xp"]
            oro = self.enemigo["oro"]

            self.jugador["xp"] += xp
            self.jugador["oro"] += oro

            self.jugador["oro_conseguido"] += oro

            self.jugador["enemigos_derrotados"] += 1

            self.enemigo = None


            mensaje += (
                f"\n\n🏆 ¡Has derrotado al {nombre}!"
                f"\n⭐ +{xp} XP"
                f"\n💰 +{oro} oro"
            )


            subida = self.comprobar_nivel()

            if subida:

                mensaje += f"\n\n{subida}"


            return {
                "mensaje": mensaje,
                "estado": self.estado()
            }


        # ----------------------------------------------------
        # TURNO DEL ENEMIGO
        # ----------------------------------------------------

        dano_enemigo = max(
            1,
            self.enemigo["ataque"]
            + random.randint(-2, 4)
            - self.jugador["defensa"]
        )


        self.jugador["vida"] -= dano_enemigo

        self.jugador["daño_recibido"] += dano_enemigo


        if self.jugador["vida"] < 0:

            self.jugador["vida"] = 0


        mensaje += (
            f"\n\n👹 {self.enemigo['nombre']} "
            f"te ha causado {dano_enemigo} "
            "de daño."
        )


        if self.jugador["vida"] <= 0:

            mensaje += (
                "\n\n💀 Has caído en combate."
            )


        return {
            "mensaje": mensaje,
            "estado": self.estado()
        }


    # ========================================================
    # USAR POCIÓN
    # ========================================================

    def usar_pocion(self):

        if self.jugador["pociones"] <= 0:

            return {
                "mensaje": "❌ No tienes pociones.",
                "estado": self.estado()
            }


        if self.jugador["vida"] >= self.jugador["vida_max"]:

            return {
                "mensaje": "❤️ Ya tienes la vida completa.",
                "estado": self.estado()
            }


        curacion = random.randint(25, 40)

        vida_anterior = self.jugador["vida"]


        self.jugador["vida"] = min(
            self.jugador["vida_max"],
            self.jugador["vida"] + curacion
        )


        vida_real = (
            self.jugador["vida"]
            - vida_anterior
        )


        self.jugador["pociones"] -= 1


        mensaje = (
            f"🧪 Has recuperado "
            f"{vida_real} puntos de vida."
        )


        # ----------------------------------------------------
        # CONTRAATAQUE
        # ----------------------------------------------------

        if self.enemigo is not None:

            dano = max(
                1,
                self.enemigo["ataque"]
                + random.randint(-2, 4)
                - self.jugador["defensa"]
            )


            self.jugador["vida"] -= dano

            self.jugador["daño_recibido"] += dano


            if self.jugador["vida"] < 0:

                self.jugador["vida"] = 0


            mensaje += (
                f"\n\n👹 {self.enemigo['nombre']} "
                f"te ha causado {dano} "
                "de daño."
            )


        return {
            "mensaje": mensaje,
            "estado": self.estado()
        }


    # ========================================================
    # HUIR
    # ========================================================

    def huir(self):

        if self.enemigo is None:

            return {
                "mensaje": "No hay ningún enemigo.",
                "estado": self.estado()
            }


        nombre = self.enemigo["nombre"]


        if random.random() < 0.50:

            self.enemigo = None

            return {
                "mensaje": (
                    f"🏃 ¡Has conseguido escapar "
                    f"del {nombre}!"
                ),
                "estado": self.estado()
            }


        dano = max(
            1,
            self.enemigo["ataque"]
            + random.randint(-2, 4)
            - self.jugador["defensa"]
        )


        self.jugador["vida"] -= dano

        self.jugador["daño_recibido"] += dano


        if self.jugador["vida"] < 0:

            self.jugador["vida"] = 0


        mensaje = (
            f"❌ ¡No consigues escapar!\n\n"
            f"👹 {nombre} te causa "
            f"{dano} puntos de daño."
        )


        if self.jugador["vida"] <= 0:

            mensaje += "\n\n💀 Has caído en combate."


        return {
            "mensaje": mensaje,
            "estado": self.estado()
        }


    # ========================================================
    # TIENDA
    # ========================================================

    def abrir_tienda(self):

        if self.enemigo is not None:

            return {
                "mensaje": (
                    "⚔️ No puedes visitar la tienda "
                    "durante un combate."
                ),
                "estado": self.estado()
            }


        self.tienda_abierta = True

        return {
            "mensaje": (
                "🏪 Bienvenido a la tienda de Auroria."
            ),
            "estado": self.estado()
        }


    def cerrar_tienda(self):

        self.tienda_abierta = False

        return {
            "mensaje": (
                "🚪 Has salido de la tienda."
            ),
            "estado": self.estado()
        }


    # ========================================================
    # COMPRAR
    # ========================================================

    def comprar(self, articulo):

        precios = {
            "pocion": 15,
            "ataque": 50,
            "defensa": 50
        }


        if articulo not in precios:

            return {
                "mensaje": "❌ Artículo desconocido.",
                "estado": self.estado()
            }


        precio = precios[articulo]


        if self.jugador["oro"] < precio:

            return {
                "mensaje": (
                    "💰 No tienes suficiente oro."
                ),
                "estado": self.estado()
            }


        self.jugador["oro"] -= precio


        if articulo == "pocion":

            self.jugador["pociones"] += 1

            mensaje = (
                "🧪 Has comprado una poción."
            )


        elif articulo == "ataque":

            self.jugador["ataque"] += 2

            mensaje = (
                "⚔️ Tu ataque ha aumentado en 2."
            )


        else:

            self.jugador["defensa"] += 2

            mensaje = (
                "🛡️ Tu defensa ha aumentado en 2."
            )


        return {
            "mensaje": mensaje,
            "estado": self.estado()
        }


    # ========================================================
    # SUBIR DE NIVEL
    # ========================================================

    def comprobar_nivel(self):

        necesario = self.jugador["nivel"] * 60


        if self.jugador["xp"] >= necesario:

            self.jugador["xp"] -= necesario

            self.jugador["nivel"] += 1

            self.jugador["vida_max"] += 20

            self.jugador["vida"] = self.jugador["vida_max"]

            self.jugador["ataque"] += 5

            self.jugador["defensa"] += 2


            return (
                f"🎉 ¡HAS SUBIDO AL NIVEL "
                f"{self.jugador['nivel']}!\n"
                "❤️ Tu vida máxima ha aumentado.\n"
                "⚔️ Tu ataque ha aumentado.\n"
                "🛡️ Tu defensa ha aumentado."
            )


        return None