# Entendiendo qué es Git y cómo funciona:

Git es un sistema de control de versiones distribuido que permite rastrear cambios en archivos y coordinar el trabajo en proyectos colaborativos. Algunos conceptos fundamentales de Git incluyen:

- **Repositorio:** Es el espacio donde se almacenan los archivos y la historia de cambios de un proyecto.
- **Commit:** Es un punto en la historia del repositorio que registra cambios en los archivos.


## Primeros Pasos en Git:

1. **Directorio de tu repo local:**
   - Abre la consola de comando y crea una carpeta donde crearas tu repositorio de git con el comando ``mkdir [nombre_de_la_carpeta]``.

2. **verifica que estas en la carpeta**
   - con ``ls -al`` mostrara el directorio en el que estas y todos los archivos que tiene dentro incluido los ocultos (los archivos ocultos empiezan por un punto)

   - utiliza ``cd [nombre_del_directorio]`` para diriguirte a un directorio, si ya tienes el directorio creado.

   - o ``cd ..`` para volver atras

3. **Inicializar un Repositorio:**
   - Para iniciar un nuevo repositorio en un directorio existente, navega a ese directorio en tu terminal y ejecuta:
     ```bash
     git init
     ```

4. **Agregar Archivos al Repositorio:**
    - Agrega archivo a tu repositorio utiliza ``touch readme.md`` para añadir un archivo reamde.md vacio a tu directorio.
   - Agrega archivos al área de preparación (staging area) con el comando `git add`, seguido del nombre del archivo o directorio:
     ```bash
     git add readme.md
     ```

5. **Hacer un Commit:**
   - Registra los cambios en el repositorio con el comando `git commit`, seguido de un mensaje descriptivo:
     ```bash
     git commit -m "Mensaje descriptivo del commit"
     ```

6. **Revisar el Historial de Commits:**
   - Para ver el historial de commits en el repositorio, utiliza el comando `git log`:
     ```bash
     git log
     ```
