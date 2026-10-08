# Proyecto Final Torneo de Videojuego.

Aplicacion Web desarrollado en Django para la gestion de un torneo de un videojuego (El juego elegido es Rocket League).

## Fases de desarrollo.

- Fase_01: Vista y modelo del formulario de registro.
- Fase_02: Vista y modelo del torneo principal del videojuego.
- Fase_03: Conexion entre paginas de inicio de sesion y torneo.
- Fase_04: Creacion de la pagina principal donde se encuentran todos los torneos.
- Fase_05: Conexion entre pagina principal y nuestros torneos.
- Fase_06: Implementacion de cierre de sesion de usuarios.
- Fase_07: Vista y modelo del formulario de inscripcion para los torneos.
- Fase_08: Construccion de la estructura principal del torneo.
- Fase_09: Panel de Admin para gestionar inscripciones.
- Fase_10: Implementacion de estadisticas en cada encuentro y en la url "/estadisticas/"

## Carpetas importantes:

- Carpeta torneo_rl: Es la carpeta principal de la aplicacion web.
- Carpeta torneo: Es la app encargada de la gestion del torneo.
- Carpeta registro: Es la app encargada del metodo de registro he inicio de sesion.
- Carpeta inscripcion: Es la app encargada de gestionar los usuarios inscritos en el torneo.
- Carpeta home: Es la app encargada de mostrar la pantalla inicial de la aplicacion web.
- Carpeta templates: Carpeta encargada de almacenar el archivo html base.

## Apps:

- Registro: Es la app que controla el registro de usuarios de la web.
- Inscripcion: Sirve para el control de registro de los participantes del torneo.
- Torneo: Es la app encargada de mostrar tanto los resultados de las fases del torneo.
- Home: Es la encargada de mostrarnos la pantalla de inicio.

## Urls.


- El home: Es la url principal donde aparecen todos los torneos.
- "/rl/": Url encargada de mostrar los datos del torneo.
- "/registro/": Url encargada de registrar usuarios
- "/login/": Es la url encargada del inicio de sesion de un usuario ya registrado
- "/inscripcion/": Url cuya funcion es mostrarnos el formulario para la inscripcion de cualquier juego teniendo en cuenta nuestro nivel.
- "/vista_torneo_rl/": Se encarga de mostrar la estructura del torneo.
- "/generador_torneo_rl/" Esta url es solo accesible para el admin. Contiene la logica para generar el llamado "Bracket".
- "/encuentros_torneo_rl/x/": Otra url solo accesible para el admin y gestiona el marcador de los encuentros.
- "/panel_admin/" Url accesible solo para el admin, que ayuda a la gestion de inscripciones.
- "/estadisticas/" Url para consultar algunas estadisticas del torneo.