// ============================================================
// LAS TIERRAS DE AURORIA
// game.js
// ============================================================


// ============================================================
// VARIABLES DEL JUEGO
// ============================================================

let enCombate = false;
let tiendaAbierta = false;

let avatarSeleccionado = "🧙‍♂️";

let estadoActual = null;


// ============================================================
// INICIO
// ============================================================

document.addEventListener("DOMContentLoaded", function () {

    prepararAvatares();

});


// ============================================================
// SELECCIÓN DE AVATAR
// ============================================================

function prepararAvatares() {

    const avatares =
        document.querySelectorAll(".avatar-opcion");


    avatares.forEach(function (boton) {

        boton.addEventListener("click", function () {

            avatares.forEach(function (otro) {

                otro.classList.remove(
                    "seleccionado"
                );

            });


            boton.classList.add(
                "seleccionado"
            );


            avatarSeleccionado =
                boton.dataset.avatar;

        });

    });

}


// ============================================================
// CREAR HÉROE
// ============================================================

async function crearHeroe() {

    const campoNombre =
        document.getElementById(
            "nombre-heroe"
        );


    const nombre =
        campoNombre.value.trim();


    if (nombre === "") {

        alert(
            "Escribe un nombre para tu héroe."
        );

        campoNombre.focus();

        return;
    }


    try {

        const respuesta =
            await fetch("/configurar", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    nombre: nombre,

                    avatar:
                        avatarSeleccionado

                })

            });


        const datos =
            await respuesta.json();


        mostrarResultado(datos);


        document.getElementById(
            "pantalla-creacion"
        ).classList.add(
            "pantalla-oculta"
        );


        document.getElementById(
            "pantalla-juego"
        ).classList.remove(
            "pantalla-oculta"
        );


        actualizarBotones();

    }

    catch (error) {

        console.error(error);

        alert(
            "No se ha podido crear el héroe."
        );

    }

}


// ============================================================
// EXPLORAR
// ============================================================

async function explorar() {

    if (enCombate) {
        return;
    }


    if (tiendaAbierta) {
        return;
    }


    const datos =
        await solicitar(
            "/explorar"
        );


    if (datos) {

        mostrarResultado(datos);

    }

}


// ============================================================
// ATACAR
// ============================================================

async function atacar() {

    if (!enCombate) {
        return;
    }


    const datos =
        await solicitar(
            "/atacar"
        );


    if (datos) {

        mostrarResultado(datos);

    }

}


// ============================================================
// USAR POCIÓN
// ============================================================

async function usarPocion() {

    const datos =
        await solicitar(
            "/pocion"
        );


    if (datos) {

        mostrarResultado(datos);

    }

}


// ============================================================
// HUIR
// ============================================================

async function huir() {

    if (!enCombate) {
        return;
    }


    const datos =
        await solicitar(
            "/huir"
        );


    if (datos) {

        mostrarResultado(datos);

    }

}


// ============================================================
// ABRIR TIENDA
// ============================================================

async function abrirTienda() {

    if (enCombate) {
        return;
    }


    if (tiendaAbierta) {
        return;
    }


    const datos =
        await solicitar(
            "/tienda"
        );


    if (!datos) {
        return;
    }


    tiendaAbierta = true;


    document.getElementById(
        "tienda"
    ).classList.remove(
        "ventana-oculta"
    );


    mostrarResultado(datos);

    actualizarBotones();

}


// ============================================================
// CERRAR TIENDA
// ============================================================

async function cerrarTienda() {

    const datos =
        await solicitar(
            "/cerrar-tienda"
        );


    tiendaAbierta = false;


    document.getElementById(
        "tienda"
    ).classList.add(
        "ventana-oculta"
    );


    if (datos) {

        mostrarResultado(datos);

    }


    actualizarBotones();

}


// ============================================================
// COMPRAR
// ============================================================

async function comprar(articulo) {

    if (!tiendaAbierta) {
        return;
    }


    const datos =
        await solicitarPost(
            "/comprar",
            {
                articulo: articulo
            }
        );


    if (datos) {

        mostrarResultado(datos);

    }

}


// ============================================================
// MOSTRAR ESTADÍSTICAS ACUMULADAS
// ============================================================

function mostrarEstadisticas() {

    if (!estadoActual) {
        return;
    }


    actualizarAcumulados(
        estadoActual
    );


    document.getElementById(
        "estadisticas-panel"
    ).classList.remove(
        "ventana-oculta"
    );


    document.getElementById(
        "boton-estadisticas"
    ).disabled = true;

}


// ============================================================
// CERRAR ESTADÍSTICAS
// ============================================================

function cerrarEstadisticas() {

    document.getElementById(
        "estadisticas-panel"
    ).classList.add(
        "ventana-oculta"
    );


    actualizarBotones();

}


// ============================================================
// PETICIÓN GET
// ============================================================

async function solicitar(url) {

    try {

        const respuesta =
            await fetch(url);


        if (!respuesta.ok) {

            throw new Error(
                "Error HTTP: " +
                respuesta.status
            );

        }


        return await respuesta.json();

    }

    catch (error) {

        console.error(error);

        mostrarErrorConexion();

        return null;

    }

}


// ============================================================
// PETICIÓN POST
// ============================================================

async function solicitarPost(
    url,
    datos
) {

    try {

        const respuesta =
            await fetch(url, {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body:
                    JSON.stringify(datos)

            });


        if (!respuesta.ok) {

            throw new Error(
                "Error HTTP: " +
                respuesta.status
            );

        }


        return await respuesta.json();

    }

    catch (error) {

        console.error(error);

        mostrarErrorConexion();

        return null;

    }

}


// ============================================================
// MOSTRAR RESULTADO
// ============================================================

function mostrarResultado(datos) {

    if (!datos) {
        return;
    }


    if (datos.estado) {

        estadoActual =
            datos.estado;

    }


    const registro =
        document.getElementById(
            "registro-texto"
        );


    if (registro && datos.mensaje) {

        registro.innerText =
            datos.mensaje;

    }


    if (estadoActual) {

        actualizarJugador(
            estadoActual
        );


        actualizarEnemigo(
            estadoActual
        );


        actualizarAcumulados(
            estadoActual
        );

    }


    actualizarBotones();

}


// ============================================================
// ACTUALIZAR DATOS DEL JUGADOR
// ============================================================

function actualizarJugador(estado) {

    const jugador =
        estado.jugador;


    if (!jugador) {
        return;
    }


    const avatar =
        document.getElementById(
            "avatar-jugador"
        );


    if (avatar) {

        avatar.innerText =
            jugador.avatar;

    }


    const nombre =
        document.getElementById(
            "nombre"
        );


    if (nombre) {

        nombre.innerText =
            jugador.nombre;

    }


    const nivel =
        document.getElementById(
            "nivel"
        );


    if (nivel) {

        nivel.innerText =
            jugador.nivel;

    }


    const xp =
        document.getElementById(
            "xp"
        );


    if (xp) {

        xp.innerText =
            jugador.xp;

    }


    const vida =
        document.getElementById(
            "vida"
        );


    if (vida) {

        vida.innerText =
            jugador.vida;

    }


    const vidaMax =
        document.getElementById(
            "vida-max"
        );


    if (vidaMax) {

        vidaMax.innerText =
            jugador.vida_max;

    }


    const ataque =
        document.getElementById(
            "ataque"
        );


    if (ataque) {

        ataque.innerText =
            jugador.ataque;

    }


    const defensa =
        document.getElementById(
            "defensa"
        );


    if (defensa) {

        defensa.innerText =
            jugador.defensa;

    }


    const oro =
        document.getElementById(
            "oro"
        );


    if (oro) {

        oro.innerText =
            jugador.oro;

    }


    const pociones =
        document.getElementById(
            "pociones"
        );


    if (pociones) {

        pociones.innerText =
            jugador.pociones;

    }


    const barraVida =
        document.getElementById(
            "barra-vida"
        );


    if (barraVida) {

        const porcentaje =
            jugador.vida_max > 0
                ? (
                    jugador.vida /
                    jugador.vida_max
                ) * 100
                : 0;


        barraVida.style.width =
            Math.max(
                0,
                Math.min(
                    100,
                    porcentaje
                )
            ) + "%";

    }


    const oroTienda =
        document.getElementById(
            "oro-tienda"
        );


    if (oroTienda) {

        oroTienda.innerText =
            jugador.oro;

    }

}


// ============================================================
// ACTUALIZAR ENEMIGO
// ============================================================

function actualizarEnemigo(estado) {

    const enemigo =
        estado.enemigo;


    const datosEnemigo =
        document.getElementById(
            "datos-enemigo"
        );


    const botonExplorar =
        document.getElementById(
            "boton-explorar"
        );


    const botonAtacar =
        document.getElementById(
            "boton-atacar"
        );


    const botonHuir =
        document.getElementById(
            "boton-huir"
        );


    const botonTienda =
        document.getElementById(
            "boton-tienda"
        );


    if (!datosEnemigo) {
        return;
    }


    // --------------------------------------------------------
    // NO HAY ENEMIGO
    // --------------------------------------------------------

    if (
        enemigo === null ||
        enemigo === undefined
    ) {

        enCombate = false;


        datosEnemigo.classList.add(
            "enemigo-oculto"
        );


        if (botonAtacar) {

            botonAtacar.disabled =
                true;

        }


        if (botonHuir) {

            botonHuir.disabled =
                true;

        }


        if (botonExplorar) {

            botonExplorar.disabled =
                tiendaAbierta;

        }


        if (botonTienda) {

            botonTienda.disabled =
                tiendaAbierta;

        }


        return;

    }


    // --------------------------------------------------------
    // HAY ENEMIGO
    // --------------------------------------------------------

    enCombate = true;


    datosEnemigo.classList.remove(
        "enemigo-oculto"
    );


    if (botonExplorar) {

        botonExplorar.disabled =
            true;

    }


    if (botonAtacar) {

        botonAtacar.disabled =
            false;

    }


    if (botonHuir) {

        botonHuir.disabled =
            false;

    }


    if (botonTienda) {

        botonTienda.disabled =
            true;

    }


    const nombreEnemigo =
        document.getElementById(
            "enemigo-nombre"
        );


    if (nombreEnemigo) {

        nombreEnemigo.innerText =
            enemigo.nombre;

    }


    const vidaEnemigo =
        document.getElementById(
            "enemigo-vida"
        );


    if (vidaEnemigo) {

        vidaEnemigo.innerText =
            enemigo.vida;

    }


    const barraEnemigo =
        document.getElementById(
            "barra-enemigo"
        );


    if (barraEnemigo) {

        const porcentaje =
            enemigo.vida_max > 0
                ? (
                    enemigo.vida /
                    enemigo.vida_max
                ) * 100
                : 0;


        barraEnemigo.style.width =
            Math.max(
                0,
                Math.min(
                    100,
                    porcentaje
                )
            ) + "%";

    }

}


// ============================================================
// ACTUALIZAR ACUMULADOS
// ============================================================

function actualizarAcumulados(estado) {

    if (!estado || !estado.jugador) {
        return;
    }


    const jugador =
        estado.jugador;


    const acumXP =
        document.getElementById(
            "acum-xp"
        );


    if (acumXP) {

        acumXP.innerText =
            jugador.xp;

    }


    const acumEnemigos =
        document.getElementById(
            "acum-enemigos"
        );


    if (acumEnemigos) {

        acumEnemigos.innerText =
            jugador.enemigos_derrotados;

    }


    const acumOro =
        document.getElementById(
            "acum-oro"
        );


    if (acumOro) {

        acumOro.innerText =
            jugador.oro_conseguido;

    }


    const acumDano =
        document.getElementById(
            "acum-dano"
        );


    if (acumDano) {

        acumDano.innerText =
            jugador.dano_causado;

    }


    const acumRecibido =
        document.getElementById(
            "acum-recibido"
        );


    if (acumRecibido) {

        acumRecibido.innerText =
            jugador.dano_recibido;

    }

}


// ============================================================
// ACTUALIZAR BOTONES
// ============================================================

function actualizarBotones() {

    const botonExplorar =
        document.getElementById(
            "boton-explorar"
        );


    const botonAtacar =
        document.getElementById(
            "boton-atacar"
        );


    const botonHuir =
        document.getElementById(
            "boton-huir"
        );


    const botonTienda =
        document.getElementById(
            "boton-tienda"
        );


    const botonEstadisticas =
        document.getElementById(
            "boton-estadisticas"
        );


    const estadisticasPanel =
        document.getElementById(
            "estadisticas-panel"
        );


    const estadisticasAbiertas =
        estadisticasPanel &&
        !estadisticasPanel.classList.contains(
            "ventana-oculta"
        );


    // --------------------------------------------------------
    // COMBATE
    // --------------------------------------------------------

    if (enCombate) {

        if (botonExplorar) {
            botonExplorar.disabled = true;
        }

        if (botonAtacar) {
            botonAtacar.disabled = false;
        }

        if (botonHuir) {
            botonHuir.disabled = false;
        }

        if (botonTienda) {
            botonTienda.disabled = true;
        }

    }

    // --------------------------------------------------------
    // TIENDA
    // --------------------------------------------------------

    else if (tiendaAbierta) {

        if (botonExplorar) {
            botonExplorar.disabled = true;
        }

        if (botonAtacar) {
            botonAtacar.disabled = true;
        }

        if (botonHuir) {
            botonHuir.disabled = true;
        }

        if (botonTienda) {
            botonTienda.disabled = true;
        }

    }

    // --------------------------------------------------------
    // EXPLORACIÓN NORMAL
    // --------------------------------------------------------

    else {

        if (botonExplorar) {
            botonExplorar.disabled = false;
        }

        if (botonAtacar) {
            botonAtacar.disabled = true;
        }

        if (botonHuir) {
            botonHuir.disabled = true;
        }

        if (botonTienda) {
            botonTienda.disabled = false;
        }

    }


    if (botonEstadisticas) {

        botonEstadisticas.disabled =
            estadisticasAbiertas ||
            tiendaAbierta ||
            enCombate;

    }

}


// ============================================================
// ERROR DE CONEXIÓN
// ============================================================

function mostrarErrorConexion() {

    const registro =
        document.getElementById(
            "registro-texto"
        );


    if (registro) {

        registro.innerText =
            "⚠️ No se ha podido conectar con el servidor.\n\n" +
            "Comprueba que Flask sigue ejecutándose " +
            "en la terminal.";

    }

}