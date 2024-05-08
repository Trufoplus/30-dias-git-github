# Git & Github desde VS Code

1. **Clonar un repositorio en Visual Studio Code**: Para ello, abre la pestaña de control de versiones (Source Control), en el panel izquierdo y ¡¡haz click en "clone repository" o "inicializar un repositorio" (si lo tienes en español).

![vscode-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vs%20code%20-%201.png)

2. **Autoriza a la aplicacion**: si es la primera vez que utilizas github desde vscode, te pedira autorizacion para conectar github con vscode.

![vscode-3](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vs%20code%20-%203.png)

3. **Selecciona el repositorio a clonar**: Una vez autorizado el acceso, te saldra un listado con los repositorios que tienes en tu cuenta de github, selecciona el que quieras clonar en tu pc.

![vscode-4](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vs%20code%20-%204.png)

4. **Trabajar con el código en Visual Studio Code**: Edita los archivos en tu proyecto según sea necesario. Te aparecera un 1 o el numero de archivos modificados marcado en la pestaña 'Source Control'

![vscode-5](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vs%20code%20-%205.png)

7. **Hacer cambios y confirmarlos**: Para agregar los cambios al stage  puedes abrir la terminal en vscode o darle al boton mas en el archivo cambiado y se te cambiará a 'staged changes'.

![vscode-6](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vs%20code%20-%206.png)

8. **Sincronización con GitHub (push)**: Una vez que hayas confirmado tus cambios, súbelos a GitHub para mantener tu repositorio remoto actualizado. Esto se puede hacer fácilmente desde Visual Studio Code, Escribe encima del boton del commit el mensaje y presiona commit, tambien puedes darle al desplegable al lado del commit y hacer commit & push y ya lo tendrias subido a tu repositorio remoto.

![vscode-7](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vs%20code%20-%207.png)

9. **Ramas**: En la esquina inferior izquierda te aparecera la rama en la que estas, en la imagen estamos en la rama 'main'

![vscode-9](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vscode%20-%209.png)

10. **Crear ramas**: Pincha en la rama main en la ezquina inferior inzquierda y se te abrira un desplegable donde podras crear una rama nueva, cambiar de rama, ver los tags, etc...

![vscode-8](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vs%20code%20-%208.png)

tambien puedes crear estas ramas, push, tag etc, haciendo click en los tres puntos en el source control:

![vscode-10](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vscode%20-%2010.png)

## Extensiones para VScode 

1. **GitLens**: Esta extensión proporciona un conjunto completo de características para mejorar la integración de Git en VS Code. Con más de 9.3 millones de descargas, GitLens ofrece representaciones visuales de commits, ramas, alijos, etiquetas y más. También incluye un paleta de comandos para ejecutar comandos de Git de manera eficiente.

![vscode-11](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/vscode%20-%2011.png)

2. **Git History**: Git History ofrece una interfaz gráfica para ver el historial de archivos, commits y cambios. Simplifica tareas como comparar archivos entre diferentes commits y buscar en el historial de commits.

3. **Git Graph**: Git Graph proporciona una representación visual de los repositorios de Git, mostrando ramas, commits y fusiones en un formato gráfico. Permite a los usuarios navegar fácilmente por la historia del repositorio.

4. **GitIgnore**: Esta extensión ofrece soporte para archivos Gitignore, simplificando el proceso de ignorar archivos o directorios específicos en un repositorio de Git. Proporciona plantillas específicas de lenguaje para crear archivos Gitignore.

    - Para añadir el .gitignore entra en la paleta de comandos (ctrl + shift + p) y escribe Add `gitignore`
    - Te aparecera un listado de lenguajes / plantillas que podras usar, por ejemplo busca python para tu proyecto de python y agrega el .gitignore para python

5. **Git Project Manager**: Git Project Manager ayuda a gestionar múltiples repositorios de Git dentro de una sola ventana de VS Code. Permite a los usuarios cambiar rápidamente entre proyectos y abrirlos en ventanas separadas.