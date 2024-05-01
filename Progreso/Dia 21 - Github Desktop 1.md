# Cómo utilizar GitHub Desktop

1. **Descarga e Instalación:**
   - Descarga GitHub Desktop desde su [sitio web oficial](https://desktop.github.com/) e instálalo en tu computadora.
   - Inicia sesión en tu cuenta de GitHub o crea una si aún no tienes una.

2. **Interfaz de Usuario:**
   - Al abrir GitHub Desktop, verás una interfaz de usuario con tus repositorios (current repository) y la actividad reciente en la parte lateral izquierda, si pinchas en "current repository", se te abrirá un desplegable donde podras añadir (add), un repositorio local existente, clonar un repositorio o crear un repositorio nuevo.

    ![desktop-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-1.png)

   - Los repositorios se muestran con iconos que indican si son públicos o privados (con una llave).

    ![desktop-3](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-3.png)

3. **Clonar Repositorio:**
   - Para clonar un repositorio existente desde GitHub, aparte del metodo anterior, puedes hacer clic en "File" y selecciona "Clone repository".
   - Aquí puedes buscar el repositorio que deseas clonar desde GitHub.

4. **Crear Nuevo Repositorio:**
   - Si deseas crear un nuevo repositorio desde cero, selecciona "File" y luego "New repository".
   - Sigue las instrucciones para configurar tu nuevo repositorio localmente.

5. **Realizar Cambios:**
   - Una vez que tengas un repositorio clonado o creado, puedes realizar cambios en los archivos directamente desde tu editor de código preferido, haciendo click en "Open in Visual Studio Code" desde la pantalla principal.

    ![desktop-7](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-7.png)

   - GitHub Desktop detectará automáticamente los cambios realizados en tus archivos.

6. **Ver Cambios Realizados:**
   - En la pestaña "History", podrás ver una lista de los archivos modificados junto con las diferencias entre las versiones anteriores (en rojo) y actuales (en verde).

   ![desktop-4](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-4.png)

   ![desktop-5](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-5.png)

7. **Hacer Commits:**
   - Para guardar tus cambios, haz un "commit", tras realizar algun cambio desde vscode. Abajo en la izquina inferior isquierda, ingresa un mensaje descriptivo que explique los cambios realizados.

    ![desktop-10](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-10.png)

8. **Sincronización con GitHub:**
   - Después de hacer commits locales, puedes sincronizar tus cambios, te apecera un mensaje en azul, indicando que tienes un archivo local esperando para se pusheado, dale al boton "push origin" en el mismo mensaje.

    ![desktop-11](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-11.png)

   - Esto enviará tus commits locales al repositorio remoto en GitHub, tambien pueder ir a la barra de arriba y hacer click en "Repository" se te abrira un desplegable donde podras hacer "push", "pull", "fetch"...

    ![desktop-13](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-13.png)

9. **Trabajar con Ramas:**
   - Puedes crear y trabajar en ramas para realizar cambios experimentales o colaborativos.
   - Usa la pestaña "Branch" para crear (New branch..), cambiar (Rename), eliminar (Delete), fusionar ramas (merge), actualizar desde el main (update from main)....

    ![desktop-17](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-17.png)

    - En "Current Branch" debajo de las pestañas, podras ver en que rama estas actualmente, ver que ramas hay, y seleccionarla para cambiar entre ramas.

    ![desktop-18](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-18.png)

    - Si abres tu repositorio en vscode para saber en que rama estas trabajando fijate en la parte inferior izquierda del programa te aparecerá el nombre de la rama actual.

    ![desktop-19](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-19.png)

10. **Gestionar Pull Requests:**
    - Si estás trabajando en un proyecto colaborativo, y estas en una rama secundaria (feature o la que sea), puedes crear pull requests para proponer cambios en el repositorio principal.
    - Usa la pestaña "Branch" y luego "create pull request" para ver y gestionar tus pull requests.

11. **Reportar Problemas:**
    - Si encuentras algún problema con GitHub Desktop, puedes reportarlo a GitHub a través de la herramienta.
    - Utiliza la opción "Help" para acceder a la documentación o para contactar con el soporte de GitHub.

12. **Finalización:**
    - Después de terminar tu trabajo, recuerda hacer un "push" final para sincronizar tus cambios con el repositorio remoto en GitHub.

13. **Actualizacion:**
    - Si ha habido cambios en el remoto, puedes actualizar tu local haciendo click en el apartado de "fetch" para ver que cambios hay.

    ![desktop-14](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-14.png)

    - Si hay algun cambio nuevo en el remoto, te saldra un mensaje en azul con el cambio, y podras darle a "pull" para traer esos cambios a tu repo.

    ![desktop-15](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-15.png)

14. **settings:**
    - En la pestaña "repository" y "repository setting" podras cambiar la direcion del remoto, los archivos que quieres ignorar y el git config.

    ![desktop-16](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/github_desktop-16.png)


