# Auroria

Auroria es un pequeño RPG desarrollado como proyecto personal para experimentar con Python y desarrollo web.

El proyecto comenzó como un juego de aventuras ejecutado desde la terminal y posteriormente evolucionó hacia una interfaz web utilizando Flask. La idea era construir algo sencillo pero suficientemente completo como para trabajar con diferentes conceptos de programación: estados de juego, combates, inventario, economía, experiencia, niveles y decisiones del jugador.

El resultado es una pequeña aventura en la que el jugador crea su personaje, explora el mundo, encuentra enemigos, combate, consigue oro y experiencia y puede utilizar una tienda para mejorar sus estadísticas.

## Características

- Creación del personaje.
- Elección entre diferentes avatares.
- Nombre personalizado para el héroe.
- Exploración del mundo.
- Encuentros aleatorios.
- Sistema de combate por turnos.
- Diferentes tipos de enemigos.
- Puntos de vida, ataque y defensa.
- Golpes críticos.
- Sistema de experiencia y niveles.
- Oro y economía.
- Inventario de pociones.
- Tienda con mejoras.
- Posibilidad de huir de los combates.
- Estadísticas acumuladas.
- Interfaz web ejecutada localmente.

## Tecnologías

El proyecto está construido principalmente con:

- Python
- Flask
- HTML
- CSS
- JavaScript

Python se encarga de la lógica del juego y Flask proporciona el servidor web. HTML y CSS forman la interfaz, mientras que JavaScript se utiliza para comunicarse con el servidor y actualizar el estado del juego sin necesidad de recargar la página.

## Estructura del proyecto

```text
auroria/
│
├── app.py
├── game.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── game.js
    └── style.css

app.py

Es el punto de entrada de la aplicación.

Se encarga de levantar el servidor Flask y definir las rutas utilizadas por la interfaz web, como explorar, atacar, usar una poción, huir, acceder a la tienda o realizar compras.

game.py

Contiene la lógica principal del juego.

Aquí se gestionan el personaje, enemigos, combates, experiencia, niveles, oro, inventario, tienda y estadísticas.

Separar esta lógica de Flask permite mantener el funcionamiento del juego independiente de la interfaz.

templates/index.html

Contiene la estructura de la interfaz web.

Incluye la pantalla de creación del personaje, información del héroe, enemigo, acciones, tienda y estadísticas.

static/game.js

Gestiona la interacción entre la interfaz y el servidor.

Realiza las peticiones a Flask y actualiza dinámicamente los elementos de la interfaz cuando cambia el estado del juego.

static/style.css

Contiene los estilos de la aplicación y adapta la interfaz a diferentes tamaños de pantalla.

Instalación

Para ejecutar Auroria localmente necesitas tener Python 3 instalado.

1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/auroria.git

Entrar en la carpeta:
cd auroria

2. Crear un entorno virtual

Es recomendable utilizar un entorno virtual para mantener las dependencias del proyecto aisladas.
En macOS y Linux: source venv/bin/activate
Activarlo: source venv/bin/activate

3. Instalar las dependencias
pip install -r requirements.txt

4. Ejecutar el juego
python3 app.py

Flask iniciará el servidor local.

Abre entonces en el navegador: http://127.0.0.1:5000

*** Cómo jugar ***

Al iniciar el juego puedes crear tu personaje seleccionando un avatar y escribiendo su nombre.

Una vez dentro de Auroria puedes explorar el mundo.

Durante la exploración pueden ocurrir diferentes eventos:

* Encontrar enemigos.
* Encontrar oro.
* Encontrar objetos.

Cuando aparece un enemigo comienza un combate.

Durante el combate puedes:

* Atacar.
* Utilizar una poción.
* Intentar huir.

Mientras estás luchando no puedes continuar explorando ni acceder a la tienda.

Al derrotar enemigos obtienes experiencia y oro. La experiencia permite subir de nivel y mejorar las características del personaje.

El oro puede utilizarse en la tienda para comprar pociones y mejoras permanentes.

Sistema de combate

El combate utiliza un sistema sencillo basado en estadísticas.

El daño producido depende principalmente del ataque del jugador y de la defensa del enemigo.

Los enemigos también pueden contraatacar después de una acción del jugador.

Existe además una posibilidad de realizar un golpe crítico que aumenta el daño producido.

El objetivo no era crear un sistema de combate complejo, sino utilizarlo como base para experimentar con estados, eventos y reglas de juego.

## Tienda

| Producto | Precio | Efecto |
|---|---:|---|
| Poción | 15 oro | Añade una poción al inventario para recuperar vida durante el combate |
| Entrenamiento | 50 oro | Aumenta el ataque del héroe en +2 |
| Armadura | 50 oro | Aumenta la defensa del héroe en +2 |

Estadísticas

El juego mantiene diferentes estadísticas acumuladas durante la partida:

* Experiencia actual.
* Enemigos derrotados.
* Oro conseguido.
* Daño causado.
* Daño recibido.

Estas estadísticas permiten tener una visión general del progreso del personaje.

Seguridad

Auroria no necesita actualmente claves de API ni credenciales externas para funcionar.

Aun así, el proyecto incluye .gitignore y .env.example como base para futuras funcionalidades que puedan requerir variables de entorno.

Las credenciales, contraseñas o claves privadas no deberían incluirse nunca directamente en el código ni subirse al repositorio.

Si en el futuro se añade una API externa, las claves deberían almacenarse como variables de entorno y no dentro de archivos JavaScript accesibles desde el navegador.

Estado del proyecto

Auroria es un proyecto personal y se encuentra en desarrollo.

La versión actual está centrada principalmente en la estructura básica del RPG y en experimentar con la conexión entre una aplicación Flask y una interfaz web.

Algunas ideas para futuras versiones:

* Guardado de partidas.
* Más zonas y localizaciones.
* Más enemigos.
* Jefes finales.
* Más objetos y equipamiento.
* Sistema de inventario más completo.
* Misiones.
* Diferentes caminos y decisiones.
* Eventos aleatorios más elaborados.
* Sistema de estadísticas más avanzado.
* Persistencia mediante una base de datos.
* Mejoras visuales de la interfaz.

Objetivo del proyecto

El objetivo de Auroria no es competir con un RPG comercial, sino utilizar un proyecto pequeño y entretenido para poner en práctica diferentes conceptos de desarrollo.

Empezó como un juego de terminal y fue evolucionando hacia una aplicación web. Esa evolución forma parte del propio proyecto y permite experimentar con diferentes capas de una aplicación: lógica, servidor, interfaz y comunicación entre ellas.

Licencia

Este proyecto se publica con fines personales y educativos.

Si decides utilizar parte del código, modificarlo o construir algo a partir de él, consulta la licencia incluida en este repositorio.