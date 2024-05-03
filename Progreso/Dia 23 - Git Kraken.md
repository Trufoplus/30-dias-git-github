# GitKraken

GitKraken ofrece una interfaz visual sofisticada con características avanzadas como la gestión de ramas y la creación de pull requests, mientras que GitHub Desktop se centra en las funciones básicas de Git, como hacer commits y sincronizar con repositorios remotos de GitHub. GitKraken es compatible con múltiples plataformas de alojamiento, como GitHub, GitLab y Bitbucket. Es una herramienta más completa que GitHub Desktop, pero solo se puede trabajar con repositorios públicos; para trabajar con repositorios privados, debes pagar.

## Descarga e instalación

1. Visita el sitio web oficial de GitKraken: [GitKraken.com](https://www.gitkraken.com/).
2. Busca la opción de descarga, que suele estar ubicada en la página de inicio o en la sección de descargas del sitio web.
3. Selecciona la versión adecuada para tu sistema operativo (Windows, macOS o Linux).
4. Una vez descargado el archivo de instalación, haz doble clic en él para iniciar el proceso de instalación.

## Uso y Manejo de GitKraken

1. **Clonar un repositorio**
    - La primera vez que abras el programa, tendrás que configurar y agregar tu cuenta de GitHub, etc.
    - Luego, se te pedirá que elijas una acción: abrir un repositorio de tu máquina local, clonar un repositorio, crear un nuevo repositorio o crear un espacio de trabajo (esto se verá más adelante).

    ![kraken-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-1.png)

    - Haz clic en "Clone repository" y tendrás varias opciones. Por ejemplo, puedes clonar con una URL que proporcionas o seleccionar un repositorio remoto de GitHub si iniciaste sesión en tu cuenta.

    ![kraken-2](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-2.png)


2. **Abrir un repositorio local**
   - Selecciona el proyecto en el que quieras trabajar.
   - Presiona "ctrl + o" o ve a "File > Open Repo" para abrir un repositorio local.
   - También puedes abrir un nuevo repositorio desde una nueva pestaña ("New Tab") y seleccionar la opción correspondiente.

   ![kraken-14](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-14.png)

3. **Ramas**
    - En la pantalla principal, podrás ver las ramas dibujadas, cómo se unen y se crean, junto con los commits.
    - Si haces clic en los commits a la derecha, verás quién lo hizo, los archivos modificados, la fecha, etc.

    ![kraken-3](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-3.png)

    - En el panel izquierdo, haz clic en los desplegables "LOCAL" y "REMOTE" para ver las ramas creadas tanto localmente como en el repositorio remoto.

    ![kraken-4](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-4.png)

    - Para crear una nueva rama, haz clic en la rama principal y selecciona "Create branch here".

4. **Modificación y commit**

   - Realiza las modificaciones necesarias en los archivos del proyecto.
   - Una vez realizados los cambios, en GitKraken aparecerá una nueva modificación con la etiqueta "//WIP".
   - Haz clic en la etiqueta y en el lado derecho podrás ver los cambios en "Unstaged Files".

   ![kraken-8](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-8.png)

   - Puedes darle al botón verde "Stage all changes" para añadir todos los archivos a "Staged Files" o seleccionar un archivo específico y darle a "Stage file".
   - Una vez que hayas añadido el archivo al "Stage File", en la parte inferior en la zona "Commit message", introduce una breve explicación para el commit y haz clic en el botón "Commit changes" para hacer el commit.

   ![kraken-9](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-9.png)

5. **Hacer Push**
   - Si deseas enviar los cambios a una rama remota, haz clic en "Push" en la barra de herramientas.
   - Selecciona la rama a la que deseas enviar los cambios y confirma.

   ![kraken-10](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-10.png)

6. **Administración de ramas**
   - Si necesitas eliminar una rama, selecciona la opción correspondiente haciendo clic en las ramas del panel izquierdo y confirma la eliminación.

   ![kraken-11](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-11.png)

   - Puedes cambiar de rama seleccionando el apartado "Branch" en la barra de herramientas.

   ![kraken-12](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-12.png)

## Crear un Workspace en GitKraken

1. Abre GitKraken y ve al área de Workspaces. Puedes acceder a esto de varias maneras:
   - En la nueva pestaña, selecciona la opción para abrir workspaces.
   - En la esquina superior izquierda, junto al ícono de la carpeta, haz clic en la pestaña "Workspaces".

    ![kraken-15](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-15.png)

2. Si es tu primera vez accediendo a esta área, es probable que esté vacía. Para crear un nuevo workspace, haz clic en el botón "New Workspace" en la esquina superior derecha.

3. Se te dará la opción de crear un "Cloud Workspace" o un "Local Workspace". Selecciona "Local Workspace".

![kraken-16](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-16.png)

4. Ahora, se te pedirá que ingreses la información para tu nuevo workspace:
   - Dale un nombre al workspace, por ejemplo, "My_Workspace".
   - Si lo deseas, puedes agregar una descripción.
   - Haz clic en el botón de "Browse repositories" para buscar la ubicación en tu pc donde se encuentran tus repositorios.

5. Navega hasta la carpeta donde tienes almacenados tus repositorios y selecciónala. Esto abrirá todos los repositorios que están dentro de esa carpeta.

6. GitKraken te mostrará una lista de todos los repositorios disponibles en la carpeta que seleccionaste. Puedes revisar esta lista y desmarcar aquellos repositorios que no deseas incluir en este workspace.

7. Una vez que hayas seleccionado los repositorios que deseas incluir, haz clic en el botón "Create Local Workspace" para crear el workspace.

¡Listo! Ahora has creado un nuevo workspace en GitKraken que contiene todos los repositorios que seleccionaste. Puedes ver una lista de estos repositorios en el área de Workspaces y comenzar a trabajar con ellos desde allí.

![kraken-17](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/kraken-17.png)
