# Sistema Experto en Anime
Sistema Experto sobre anime desarrollado con Python

## Características
- Usando como motor de inferencia PyMySQL
- Base de hechos en MySQL
- Interfaz Gráfica de Usuario (GUI) con Qt, PyQt

## Requisitos previos

Antes de instalar y ejecutar esta API, asegúrate de tener instaladas las siguientes herramientas:

- Python (versión 3.7 o superior)
- Pip (gestor de paquetes de Python)
- MySQL
- PhpMyAdmin (opcional)
- XAMPP (opcional)

`https://www.python.org/downloads/`

## Instalación

1. Clona este repositorio en tu máquina local:
<pre><code> git clone https://github.com/PeterPerez01/sistemaexperto_anime.git </code></pre>

  1.1 Enciende tu sistema gestor de bases de datos
  1.2 Importa la base de datos 'animes.sql'
  
  En XAMPP sigue los siguientes pasos:
  1. Ejecuta XAMPP
  2. Activa el MySQL
  3. Activa Apache
  4. Ingresa a la dirección 'localhost/' en tu navegador
  5. En el menú superior selecciona PhpMyAdmin
  6. Al ingresar, haz clic en 'Crear nueva base de datos'
  7. Crea una base de datos con el nombre 'animes'
  8. Una vez creada haz clic en ella y luego selecciona la opción importar del menú superior derecho
  9. haz clic en 'Seleccionar Archivo' y selecciona el archivo 'animes.sql'
  10. Ve hasta el final de la página y selecciona continuar
  11. Acepta y una vez importada la base de datos prosigue con el siguiente paso

2. Accede al directorio del repositorio:
<pre><code> cd sistemaexperto_anime </code></pre>


3. Crea un entorno virtual para el proyecto:
<pre><code>python -m venv venv</code></pre>


4. Activa el entorno virtual:

- En Windows:

  ```
  venv\Scripts\activate
  ```

- En Linux o macOS:

  ```
  source venv/bin/activate
  ```

5. Instala las dependencias del proyecto:
<pre><code> pip install -r requirements.txt </code></pre>

6. Ejecuta el sistema:
Entra en la carpeta raíz del proyecto y abre una consola para ejecutar el comando
<pre><code> python SistemaAnime.py </code></pre>


¡Todo listo! esta todo perfectamente configurado y listo para funcionar.


## Uso

Selecciona desde el combobox la configuración de lo que deseas consultar.
En caso de no existir alguna coincidencia puedes acceder al Panel Experto para agregar nuevas opciones, ramas o respuestas.



## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama para tu nueva característica o corrección de errores: `git checkout -b nueva-caracteristica`.
3. Realiza los cambios necesarios y commitea tus modificaciones: `git commit -am 'Agrega nueva característica'`.
4. Envía tus cambios a tu repositorio remoto: `git push origin nueva-caracteristica`.
5. Abre una pull request en este repositorio.

¡Agradecemos todas las contribuciones!

## Licencia

Este proyecto se encuentra bajo la [Licencia MIT](LICENSE).

