# ¿Qué es Git Stash?
Git Stash es una característica de Git que te permite guardar temporalmente cambios en tu directorio de trabajo sin necesidad de hacer commit. Esto es útil cuando estás en medio de trabajar en una rama y necesitas cambiar rápidamente a otra tarea, pero no quieres hacer un commit de tus cambios parciales.


# ¿Cómo usar Git Stash?
### 1. Guardar cambios en el stash
````bash
git stash save "Mensaje opcional"
````
Este comando guarda los cambios que tienes en tu directorio de trabajo en el stash. Puedes agregar un mensaje opcional para describir los cambios que estás guardando.


### 2. Ver lista de stashes:
````bash
git stash list
````
Este comando muestra una lista de todos los stashes que has guardado en tu repositorio.
Algo como esto:
````bash
stash@{0}: On master: Cambios temporales para arreglar el bug #123
stash@{1}: On feature-branch: Cambios para pruebas de rendimiento
`````


### 3. Aplicar los cambios del stash:
````bash
git stash apply

````
Este comando aplica los cambios del último stash guardado al trabajo que estamos desarrollando, pero los cambios permanecen en el stash. Pero este comando se selecciona concretamente el último stash de la pila, no obstante, es posible elegir los que nosotros queramos aplicar, por ello se usa el comando `git stash apply stash@{n}` donde n es el numero de stash.


### 4. Eliminar un stash:
````bash
git stash drop
````
Este comando elimina el último stash guardado. Si quieres eliminar un stash específico, puedes usar `git stash drop stash@{n}`.


### 5. Aplicar y eliminar los cambios del stash:
````bash
git stash pop
````
Toma un cambio almacenado, lo elimina de la "pila de almacenamiento" y lo aplica al árbol de trabajo actual



# Ejemplo de uso:
Supongamos que estás trabajando en una nueva función en una rama llamada feature-branch, pero te interrumpen con una solicitud urgente de corrección de errores en la rama master. En lugar de hacer un commit con tus cambios parciales en feature-branch, puedes usar Git Stash:

**1.** Guardas tus cambios en el stash:
````bash
git stash save "Cambios en la función nueva"
````
**2.** Cambias a la rama master y haces las correcciones necesarias.

**3.** Cuando terminas con las correcciones, vuelves a tu rama feature-branch y recuperas tus cambios del stash:

````bash
git checkout feature-branch
git stash pop
````
Ahora puedes continuar trabajando en tu función nueva sin perder los cambios que hiciste previamente.


# Visualización detallada de cambios en un stash:
### 1. Mostrar descripciones de stashes con estadísticas:
````bash
git stash list --stat
````
Este comando muestra una lista de todos los stashes con descripciones breves y estadísticas de los cambios en cada uno.

Algo como esto:
````bash
stash@{0}: On master: Cambios temporales para arreglar el bug #123
 stash@{1}: On feature-branch: Cambios para pruebas de rendimiento
  archivo_modificado1.txt  |  12 ++++++++++++
  archivo_modificado2.txt  |   7 +++++++
 2 files changed, 19 insertions(+)
````

### 2. Mostrar cambios detallados en un stash:
````bash
git stash show -p stash@{n}
````
Este comando muestra los cambios detallados en un stash específico, incluyendo el diff de cada archivo modificado.

### Crear una rama a partir de un stash:
````bash
git stash branch nombre_de_la_rama ID_del_stash
````
Este comando crea una nueva rama a partir de un stash específico, permitiéndote trabajar en los cambios guardados en ese stash en un entorno separado.

Ejemplo:

````bash
git stash branch nueva-rama stash@{1}
````
Con este comando, se creará una nueva rama llamada nueva-rama a partir del stash identificado como stash@{1}.