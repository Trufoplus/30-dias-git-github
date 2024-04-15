# RAMAS
## ¿Qué son las ramas en Git?
Cuando trabajamos en Git, normalmente lo hacemos en la rama principal llamada "Main". Sin embargo, Git nos permite crear ramas adicionales que nos permiten trabajar en áreas separadas sin afectar el trabajo de otros desarrolladores.

![The Markdown logo](https://www.nobledesktop.com/image/gitresources/git-branches-merge.png)


## ¿Por qué son importantes las ramas?
Imagina una empresa con varios desarrolladores. Si todos trabajan en la misma rama y algo sale mal, todos se ven afectados. Por eso, es útil que cada desarrollador trabaje en su propia rama para desarrollar nuevas funciones o características sin interferir con el trabajo de los demás.

## ¿Cómo funcionan las ramas?  (merge)
Cuando creamos una nueva función, creamos una nueva rama para trabajar en ella. Una vez que la función está completa, la combinamos con la rama principal (Main) en un proceso llamado "merge". Esto nos permite mantener un proyecto limpio y organizado, con una rama principal que representa el proyecto completo y ramas secundarias para nuevas funciones.

# Tipos de ramas:
![The Markdown logo](https://www.atatus.com/blog/content/images/2021/06/git-branch-workflow-2.png)

## Ramas principales:
* Main: Esta es la rama principal y estable del proyecto. Aquí se encuentra el código en producción.

* Develop: Esta rama es donde se integran todas las características completadas y se preparan para la próxima versión.

## Ramas auxiliares:

* Feature: Se utiliza para desarrollar nuevas características o funcionalidades. Es una rama temporal que se crea y elimina después de completar la tarea.

* Release: Se crea a partir de la rama Develop para preparar una versión para producción. Se realizan pruebas finales y correcciones de errores antes de fusionarla con Main.

* Hotfix: Se usa para solucionar problemas críticos en producción de forma rápida. Se crea a partir de Main, se corrige el problema y se fusiona tanto con Main como con Develop.

## ¿Por qué tantos tipos de ramas?
Cada tipo de rama tiene un propósito específico para mantener un flujo de trabajo ordenado y minimizar el riesgo de errores en el código de producción. Es importante seguir esta metodología para evitar problemas inesperados al integrar código en las ramas principales como Main o Develop.

## ¿Cómo funcionan las ramas auxiliares?
Cada tipo de rama auxiliar tiene un inicio y un fin definidos. Una vez que se completa la tarea o se corrige el problema, la rama se fusiona con la rama principal correspondiente (Main o Develop). Esto significa que las ramas auxiliares tienen una vida temporal y se eliminan después de que su funcionalidad se integra en Main.

## Listar y crear ramas:
Utilizamos el comando ```git branch``` para ver las ramas disponibles en nuestro proyecto. La rama actual está marcada con un asterisco.

Para crear una nueva rama, usamos ```git branch <nombre de la rama>```.

## Cambiar entre ramas:
Utilizamos `git checkout <nombre de la rama>` para cambiarnos a la nueva rama que creamos.


# **MERGE**
## Tipos de merge:

### Fast-forward merge:
En este tipo de merge, la rama principal (normalmente "main") no ha cambiado desde que se creó la rama secundaria. Por lo tanto, los cambios realizados en la rama secundaria se pueden fusionar directamente con la rama principal sin conflictos.

### Unión automática:
En este caso, tanto la rama secundaria como la rama principal han experimentado cambios. Sin embargo, estos cambios son independientes entre sí, lo que significa que no hay conflictos al fusionar las ramas. Git puede unir automáticamente los cambios de ambas ramas sin problemas.

### Merge con conflictos:
Aquí es donde las cosas se complican. Si dos ramas han realizado cambios en el mismo archivo, Git no puede determinar automáticamente qué cambios conservar. Esto resulta en un conflicto de merge, donde se requiere la intervención manual del usuario para resolver los conflictos y decidir qué cambios mantener.

## Como hacer un Merge Fast-Forward:

Primero, no situamos en la rama "master" con el comando `git checkout main`.
Luego, simplemente ejecutamos `git merge <nombre de la rama>` para fusionar los cambios de la rama "derivadas" en "main".
Esto realiza un "merge fast-forward", que es posible cuando la rama principal no ha tenido cambios desde que se creó la rama secundaria.

## Eliminar la rama secundaria:

Después de fusionar los cambios, la rama "derivadas" ya no es necesaria y podemos eliminarla para mantener el proyecto limpio.

Utilizamos `git branch -d <nombre de la rama>` para eliminar la rama secundaria. Por ejemplo, git branch -d derivadas.

## Verificar el estado del proyecto:

Finalmente, podemos verificar que solo tenemos la rama "main" y que los cambios de "derivadas" se han fusionado correctamente con `git branch`.
Este proceso garantiza que todas las nuevas funcionalidades desarrolladas en la rama "derivadas" se incorporen de manera segura en la rama principal "main". Mantener un proyecto limpio y organizado es fundamental para facilitar la colaboración y el mantenimiento a largo plazo.



## Como hacer una Union Automcatica
### 1. Crear una nueva rama y realizar cambios:
Utilizamos `git checkout -b <nombre de la rama>` para crear y cambiar a una nueva rama en un solo paso. 

Por ejemplo: 
```bash
git checkout -b integrales.
```
Hacemos cambios en los archivos de esa rama, como crear y editar el archivo "Integrales.py".

### 2. Cambios en la rama principal (main):
Nos movemos de vuelta a la rama "main" con `git checkout main`.
Realizamos cambios en la rama "main", como editar el archivo "derivadas.py".

En este punto tenemos que la rama main a cambiado antes de haber unido la rama "integrales".

### 3. Realizar un merge automático:
Ejecutamos `git merge <nombre de la rama>` para fusionar los cambios de la rama "integrales" en la rama "master". 

Por ejemplo: 
```bash
git merge integrales
```
Git puede fusionar automáticamente los cambios de ambas ramas sin conflictos.

### 4. Verificar y limpiar:
Utilizamos `git log --oneline --decorate --all --graph` para verificar que los cambios se han fusionado correctamente en la rama "main".

veremos algo como la siguiente imagen:

```markdown
*   f8fb185 (HEAD -> main) Merge branch 'integrales'
|\
| * 688d8eb Script para hacer integrales
* | c33aa79 Script de derivadas sin integrales
|/
* 516268e Script para hacer derivadas
```

Finalmente, eliminamos la rama "integrales" con `git branch -d integrales` para mantener el proyecto limpio y organizado.


## Merge con Conflictos en Git
### 1. Creación de una rama y realización de cambios:
Utilizamos git checkout `-b <nombre de la rama>` para crear y cambiar a una nueva rama en un solo paso.
Por ejemplo:
```bash
git checkout -b integrales-modificadas
```
Realizamos cambios en los archivos de esa rama, como editar el archivo "Integrales.py".

### 2. Cambios en la rama principal (main):
Nos movemos de vuelta a la rama "main" con `git checkout master`.
Realizamos cambios en la rama "main", como editar el archivo "Integrales.py".

### 3. Realización de un merge con conflictos:
Ejecutamos `git merge <nombre de la rama>` para fusionar los cambios de la rama "integrales-modificadas" en la rama "main".
Por ejemplo:
````bash
git merge integrales-modificadas
````
Se producirá un conflicto si ambas ramas han modificado las mismas líneas del archivo.
```` bash
Auto-merging integrales.py
CONFLICT (content): Merge conflict in integrales.py
Automatic merge failed; fix conflicts and then commit the result.
````
### 4. Solución de conflictos:
Abrimos el archivo en conflicto en vscode.
Buscamos las secciones marcadas como conflictivas y decidimos qué cambios mantener.
````python
<<<<<<< HEAD
print("Esto es una integral que me gusta mucho")
=======
print("Esto es una integral muy chula")
print("Esto va a entrar en conflictos")
>>>>>>> integrales-modificadas
````
De el igual hacia arriba vemos la linea modificada en el main, del igual hacia abajo vemos las lineas modificada en la rama "integrales-modificadas", simplemente decidimos con que linea de las dos nos quedamos y borramos la otra
Guardamos el archivo y volvemos al terminal.

### 5. Confirmación de los cambios:
Añadimos el archivo solucionado al área de preparación con `git add <nombre del archivo>`.
Realizamos un commit para confirmar los cambios con git `commit -m "Mensaje descriptivo"`.

### 6. Finalización del proceso:
Verificamos que no hay más conflictos con `git status`.
Borramos la rama "integrales-modificadas" con `git branch -d integrales-modificadas`.
Este proceso asegura que los cambios se fusionen correctamente y que no se pierdan modificaciones importantes durante el proceso de fusión.
