# Clonación de repositorios

1. **Identificar el Repositorio a Clonar**: Selecciona el repositorio que deseas clonar en GitHub.

2. **Seleccionar el Método de Clonación**: Pincha en el boton **code**, dale a la pestaña **Local** y escoge entre HTTPS, SSH, o GitHub CLI según tu preferencia personales, necesidades de seguridad y nivel de familiaridad con las herramientas, tambien se puede descargar directamente pinchando en 'download zip', pero nosotros usaremos linea de comando con **HTTPS** (es el metodo que menos problemas suele dar).

![clone_3](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/clone_3.png)

3. **Copiar el Comando de Clonación**: Copia la URL proporcionado para el método seleccionado, haciendo click en el icono de 'copiar' (ver imagen).

![clone_1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/clone_1.png)

4. **Abrir la Terminal y Navegar a la Ubicación Deseada**: Utiliza `cd` en la terminal para ir a la ubicación deseada en tu sistema y 'mkdir [nombre_de_la_carpeta]' para crear la carpeta donde quieras que se clone el repositorio.

5. **Ejecutar el Comando de Clonación**: Ejecuta el comando de clonación en la terminal ``git clone [URL]``.

![clone_12](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/clone_2.png)

6. **Verificar la Clonación**: Confirma que el repositorio se ha clonado correctamente, con ``git log`` podras ver todos los commits hechos en ese repositorio.

7. **Explorar y Trabajar con el Repositorio Clonado**: Explora el contenido del repositorio clonado y comienza a trabajar en él.

8. **Eliminar el Repositorio Clonado (Opcional)**: Si ya no necesitas el repositorio clonado, puedes eliminarlo de tu máquina local usando el comando en la consola ``rm -rvf [nombre_de_carpeta]``.

La clonación de repositorios en GitHub es esencial para colaborar en proyectos y trabajar de manera efectiva en un entorno de desarrollo colaborativo.


## Crear archivos desde GitHub

1. **Acceder al repositorio en GitHub**: Navegar al repositorio en GitHub donde deseas crear el nuevo archivo.

2. **Hacer clic en "add file"**: Buscar el botón 'add file' y luego 'create new file' o enlace que permita crear un nuevo archivo en el repositorio y hacer clic en él.

3. **Nombre el archivo**: En el campo "Name your file", ingresar el nombre que deseas para tu archivo. Por ejemplo, "historia.md" para crear un archivo de texto markdown.

![archivo_8](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/archivo_8.png)

4. **Escribir el contenido**: En el área de edición del archivo, comenzar a escribir el contenido del archivo. Se puede copiar y pegar el texto proporcionado como referencia o escribir tu propio contenido.


5. **Insertar imágenes (opcional)**: Si deseas insertar una imagen en tu archivo, puedes hacerlo utilizando Markdown. Utilizar el formato `![texto_alternativo](URL_de_la_imagen)` o simplemente arrastra la imagen desde la web o desde tu repositorio hasta el area de edicion del archivo.

6. **Revisar y realizar cambios (opcional)**: Una vez que se haya escrito todo el contenido y realizado los cambios necesarios, se puede revisar el archivo utilizando la opción de previsualización (preview), al lado de la opcion de 'edit'.

![archivo_1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/archivo_1.png)

7. **Realizar un commit**: En la esquina superior derecha de la página y encontraras un boton para hacer commit (commit changes...) haz click en el y proporciona un mensaje descriptivo donde pone 'commit message', como "historia de git", en 'extended descripcion' lo dejamo en blanco, es para dar una descripcion mas detallada opcional.

![archivo_2](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/archivo_2.png)

8. **Cambiar de rama**: en la parte baja podemos seleccionar si publicarlo directamente en la rama principal (main) o en una nueva rama y le daremos un nombre a esta nueva rama (historia-git). Acto seguido haremos el commit dandole a 'Propose changes'

![archivo_3](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/archivo_3.png)

9. **Crear un pull request**: Si desea fusionar los cambios, se puede crear un pull request. Proporcionar una descripción clara de los cambios en el pull request.

10. **Completar el pull request**: Si todo está bien y se está listo para fusionar los cambios, se puede completar el pull request y luego hacer un "merge" para fusionar los cambios en el proyecto.

11. **Actualizar el repositorio local (opcional)**: Si se está trabajando en una copia local del repositorio, se pueden utilizar los comandos `git fetch` y `git pull` para sincronizar los cambios realizados en GitHub con el repositorio local.
Primero haremos un `git fetch`, para ver los cambios que se han hecho:

![archivo_7](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/archivo_7.png)

aqui podemos ver el hash de un nuevo archivo y tambien la creacion de una nueva rama llamada 'historia---git'

hacemos un `git pull` para unir los cambios del remoto en el local.

### consideraciones fallos comunes:

si hacemos `git branch` es posible que la nueva rama no aparezca, esto es porque habeses no se actualiza correctamente, para esto nos cambiaremos a la rama nueva con ``git checkout historia---git``, de esta forma ya aparecera la rama en nuestro repositorio local, vuelve a hacer ``git brach`` para comprobarlo


# Explicación detallada de los commits en Git

Los commits en un repositorio Git son instantáneas de los cambios que has hecho en tus archivos en un momento específico. Cada commit captura un conjunto de cambios y los guarda en el historial de tu repositorio, lo que te permite realizar un seguimiento de la evolución de tu proyecto y revertir a versiones anteriores si es necesario.

## Puntos clave:

1. **Descripción del commit**: Cada commit tiene una descripción que proporciona información sobre los cambios realizados. Esta descripción se utiliza para comunicar qué cambios se han realizado en este commit en particular.

2. **Ramificación (Branching)**: Los commits pueden realizarse tanto en la rama principal (en este caso, "Main") como en otras ramas. Es importante tener en cuenta en qué rama estás trabajando al realizar un commit, lo mas recomendado es trabajar en ramas secundarias, por si hay algun error no te carges la rama principal main.

3. **Revisión de los cambios**: Antes de realizar un commit, es importante revisar cuidadosamente los cambios realizados para asegurarse de que son correctos y están completos.

4. **Descripción extendida**: Además de la descripción del commit, es posible incluir una descripción extendida que proporcione más detalles sobre los cambios realizados. Esto puede ser útil, especialmente cuando se trabaja en equipo, para proporcionar contexto adicional sobre los cambios. 

si vas a tu proyecto principal y mantienes el cursor sobre el commit veras la descripcion avansada.

![commmit-4](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/commit_4.png)

5. **Visualización de cambios**: Haz click sobre el commit (imagen arriba) Los commits muestran claramente qué se ha añadido (en verde) y qué se ha eliminado (en rojo) en cada cambio realizado. Esto facilita la comprensión de los cambios realizados en el código.

![commmit-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/commit_1.png)

6. **Interacción con otros desarrolladores**: Los comentarios en los commits permiten a los miembros del equipo proporcionar retroalimentación sobre los cambios realizados. Esto puede incluir haciendo click en el simbolo '-' que hay al lado de la linea cambiada (ver imagen abajo), y añadir sugerencias de mejoras o preguntas sobre por qué se realizaron ciertos cambios.

![commmit-2](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/commit_2.png)


7. **Interactividad**: Es posible interactuar con los comentarios en los commits, lo que incluye dejar respuestas, valoraciones o realizar ediciones en los comentarios existentes.

![commmit-3](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/commit_3.png)

En resumen, los commits en Git son una parte fundamental del proceso de desarrollo de software, ya que permiten realizar un seguimiento de los cambios, colaborar con otros desarrolladores y mantener un historial detallado de la evolución del proyecto.


