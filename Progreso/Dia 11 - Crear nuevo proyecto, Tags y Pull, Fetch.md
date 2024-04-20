# Crear un Proyecto en GitHub


1. **Inicia sesión en tu cuenta de GitHub:** Accede a tu cuenta en GitHub con tus credenciales.

2. **Navega a la página principal:** Una vez que hayas iniciado sesión, ve a la página principal de GitHub, haciendo click en el simbolo de github o en la pestaña donde pone "home".

3. **Haz clic en el botón "New":** Busca el botón "New" en la página principal y haz clic en él.

![creando_repositorio_remoto_1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/creando_repositorio_remoto_1.png)

4. **Crea un nuevo repositorio:** En la página que se abre, verás la opción de crear un nuevo repositorio. Introduce un nombre para tu repositorio. Por ejemplo, puedes llamarlo "proyecto-mates".

![creando_repositorio_remoto_2](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/repository_name.jpg)

5. **Añade una descripción (opcional):** Si lo deseas, puedes añadir una breve descripción para tu repositorio. Por ejemplo, "Este es nuestro repositorio remoto para nuestro proyecto de matemáticas."

![respository_description](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/repository_description.png)

6. **Selecciona la visibilidad del repositorio:** Elige entre público o privado según tus preferencias. Si es público, cualquier persona podrá verlo; si es privado, solo los miembros de tu equipo u organización podrán acceder.

![repository_public_or_private](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/repository_public_or_private.jpg)

7. **Inicializa el repositorio:** Si lo deseas, puedes inicializar el repositorio con un archivo README, agregar un archivo .gitignore o seleccionar una licencia. Si no necesitas ninguno de estos, puedes pasar este paso.

![repository_with](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/repository_with.png)

8. **Crea el repositorio:** Una vez que hayas completado los pasos anteriores, haz clic en el botón para crear el repositorio.

![repository_create](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/repository_create.png)

9. **Configura tu repositorio local:** Ahora necesitas configurar tu repositorio local para que esté vinculado con el repositorio remoto en GitHub.


10. **Abre la terminal:** Ve a la terminal en tu computadora.

11. **Navega a tu proyecto local:** Utiliza el comando `cd` para navegar hasta el directorio donde se encuentra tu proyecto local. una `mkdir` para crear una nueva carpeta.

12. **Inicializa el repostirio remoto:** Utiliza el comando `git init` para inicializar el repositorio local en la carpeta de tu proyecto local.

12. **Agrega el origen remoto:** Utiliza el comando `git remote add origin` seguido de la URL del repositorio remoto que has creado en GitHub. Por ejemplo:
    ```
    git remote add origin <URL_del_repositorio>
    ```

13. **Importa la rama principal:** Utiliza el comando `git branch` para importar la rama principal del repositorio remoto. Por ejemplo:
    ```
    git branch -M main
    ```

14. **Envía tu código al repositorio remoto:** Utiliza el comando `git push` seguido del nombre del origen (`origin`) y el nombre de la rama (`main`). Por ejemplo:
    ```
    git push -u origin main
    ```

15. **Verifica el estado:** Después de ejecutar el comando de envío, verifica que no haya errores y que tu código se haya enviado correctamente al repositorio remoto.

¡Y eso es todo!

# Añadiendo Tags en GitHub

1. Abre la terminal y navega hasta el directorio de tu proyecto utilizando el comando `cd`.

2. Verifica que estás en la rama correcta ejecutando el comando `git branch`. Si necesitas cambiar de rama, utiliza `git checkout <nombre_de_la_rama>`.

3. Ejecuta el comando `git tag` para ver las versiones etiquetadas que has creado hasta ahora. Asegúrate de tener claro qué nombres de etiquetas deseas usar. 

4. Para crear un nuevo tag, utiliza el comando `git tag <nombre_del_tag>`. Por ejemplo, si quieres etiquetar la versión 1 de tu proyecto, puedes escribir `git tag v1.0.0`.

````bash
git tag -a v1.0.0Alpha -m "Primera version casi lista pero inestable"
````

5. Para enviar los tags al repositorio remoto en GitHub, necesitas ejecutar el comando `git push origin --tags`. Esto asegurará que los tags también estén disponibles en GitHub.

6. Una vez que hayas hecho esto, ve a la página de tu repositorio en GitHub y verifica que los tags se hayan agregado correctamente. Puedes encontrarlos en la pestaña "Tags" en la parte superior de la página del repositorio.

![tags 1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/tags%201.png)

Si haces click en el simbolo de tags, podras ver un listado con las tags o versiones de tu proyecto.

![tags 2](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/tags%202.png)

Si haces click en el tags, podras verlo con mas detalles y incliso comprarla con otros tags de tu proyecto

![tags 3](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/tags%203.png)

# GIT FETCH & GIT PULL

desde nuestro github, podemos abrir un archivo, por ejemplo el README.md y modificarlo dandole al simbolo del lapiz arriba a la izquierda, y se nos abrira el editor. añadimos unas lineas y pinchamos en commit para committear los cambios.

![pull_1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/pull_1.png)

en el commit nos da las opciones de darle una descripcion y tambien debajo podemos seleccionar si lo queremos commitear en la rama principal (main) o seleccionar otra rama.

![pull_2](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/pull_2.png)

- **git fetch**: Este comando permite recibir todas las modificaciones que se han realizado en el repositorio remoto, pero no las aplica directamente en el proyecto local. Al ejecutar `git fetch`, se obtiene información sobre los cambios que se han realizado en el repositorio remoto, pero no se actualiza automáticamente el proyecto local. Es como si se "recogieran" los cambios para tenerlos disponibles, pero aún no se integran en el proyecto local.

![pull_4](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/pull_4.png)

En la imagen marcado en amarillo nos dice que el repositorio remoto tiene un commmit que no tenemos en nuestro local. los nuemros y letras serian el hash de dicho commit.

- **git pull**: Por otro lado, `git pull` descarga directamente los cambios desde el repositorio remoto y los aplica automáticamente al proyecto local. Es una combinación de los comandos `git fetch` y `git merge`, donde primero se recogen los cambios del repositorio remoto y luego se integran en el proyecto local. Al ejecutar `git pull`, se obtienen los cambios del repositorio remoto y se aplican directamente en el proyecto local.

![pull_5](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/pull_5.png)

tal y como vemos en la imagen, al hacer pull nos indica un cambio en el archivo README.md y que este archivo tiene 3 nuevas lineas agregadas que se han integrado sin ningun conflicto con nuestro archivo local.

Es importante tener en cuenta que al utilizar `git pull`, los cambios del repositorio remoto se integran automáticamente en el proyecto local, lo que puede generar conflictos si hay modificaciones locales que entran en conflicto con los cambios remotos. Por eso, es recomendable revisar los cambios obtenidos mediante `git fetch` antes de aplicarlos con `git pull`, para evitar posibles conflictos y asegurarse de que los cambios se integren de manera adecuada en el proyecto local.
