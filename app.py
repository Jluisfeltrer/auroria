from flask import Flask, render_template, jsonify, request

from game import Juego


# ============================================================
# CONFIGURACIÓN
# ============================================================

app = Flask(__name__)


# ============================================================
# PARTIDA
# ============================================================

juego = Juego()


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

@app.route("/")
def inicio():

    return render_template(
        "index.html",
        estado=juego.estado()
    )


# ============================================================
# CREAR / CONFIGURAR HÉROE
# ============================================================

@app.route("/configurar", methods=["POST"])
def configurar():

    datos = request.get_json()

    nombre = datos.get("nombre", "Héroe")

    avatar = datos.get("avatar", "🧙‍♂️")


    estado = juego.configurar_personaje(
        nombre,
        avatar
    )


    return jsonify({
        "mensaje": (
            f"⚔️ ¡Bienvenido, "
            f"{juego.jugador['nombre']}!"
        ),
        "estado": estado
    })


# ============================================================
# EXPLORAR
# ============================================================

@app.route("/explorar")
def explorar():

    resultado = juego.explorar()

    return jsonify(resultado)


# ============================================================
# ATACAR
# ============================================================

@app.route("/atacar")
def atacar():

    resultado = juego.atacar()

    return jsonify(resultado)


# ============================================================
# POCIÓN
# ============================================================

@app.route("/pocion")
def pocion():

    resultado = juego.usar_pocion()

    return jsonify(resultado)


# ============================================================
# HUIR
# ============================================================

@app.route("/huir")
def huir():

    resultado = juego.huir()

    return jsonify(resultado)


# ============================================================
# ABRIR TIENDA
# ============================================================

@app.route("/tienda")
def tienda():

    resultado = juego.abrir_tienda()

    return jsonify(resultado)


# ============================================================
# CERRAR TIENDA
# ============================================================

@app.route("/cerrar-tienda")
def cerrar_tienda():

    resultado = juego.cerrar_tienda()

    return jsonify(resultado)


# ============================================================
# COMPRAR
# ============================================================

@app.route("/comprar", methods=["POST"])
def comprar():

    datos = request.get_json()

    articulo = datos.get("articulo")


    resultado = juego.comprar(articulo)

    return jsonify(resultado)


# ============================================================
# ARRANCAR SERVIDOR
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)