# TAGS

## ¿Que es un TAG?

---

Los tags son como etiquetas que le pones a versiones importantes de tu proyecto. Imagina que estás escribiendo un libro y cada vez que haces cambios grandes, como terminar un capítulo, pones una etiqueta para marcar ese momento. Por ejemplo, podrías tener un tag que diga "Capítulo 1 terminado" o "Versión 1.0" si ya terminaste la primera versión completa del libro.

Estas etiquetas te ayudan a encontrar fácilmente esos puntos importantes en el historial de cambios de tu proyecto. Son como marcadores que te permiten regresar a versiones específicas del libro sin tener que revisar todo el historial de cambios. Digamos que has etiquetado una versión de tu proyecto con "Versión 1.0". Si alguien quiere ver exactamente cómo era tu proyecto en esa versión, puede simplemente seleccionar ese tag en la plataforma (en GitHub, por ejemplo) y verá todos los archivos y el estado del proyecto en ese momento.

![etiquetas](https://miro.medium.com/v2/resize:fit:1400/1*9yJY7fyscWFUVRqnx0BM6A.png)


## Generacion de TAGS

---

### 1. Comando básico:
Para crear una etiqueta simple, utilizas el comando `git tag [nombre_de_la_etiqueta]`. 

Por ejemplo:

````bash
git tag v1.0.0
````
---

### 2. Etiqueta con mensaje:

Puedes añadir un mensaje descriptivo a tu etiqueta utilizando el flag -m:

````bash
git tag -a v1.0.0 -m "Primera versión estable del proyecto"
````
Esto crea una etiqueta llamada "v1.0.0" con el mensaje asociado.

---

### 3. Ver etiquetas existentes:
Puedes ver todas las etiquetas existentes en tu repositorio con el comando git tag. 
Por ejemplo:
````bash
git tag
````
Esto mostrará una lista de todas las etiquetas disponibles en tu proyecto.

---

### 4. Eliminar una etiqueta:
Si necesitas eliminar una etiqueta, puedes utilizar el comando `git tag -d nombre_de_la_etiqueta`. 
Por ejemplo:
````bash
git tag -d v1.0.0
````

---

### 5. Ir a una versión específica:
Si deseas volver a una versión específica de tu proyecto, simplemente puedes cambiar a esa etiqueta.
Por ejemplo:
````bash
git checkout v1.0.0
````
Esto cambiará tu proyecto a la versión etiquetada como "v1.0.0".

Verás el mensaje "You are in 'detached HEAD' state", significa que estás en un estado conocido como "detached HEAD" en Git. Esto ocurre cuando has cambiado a un commit específico en lugar de a una rama. En este estado, puedes realizar cambios experimentales y hacer commits, pero estos cambios no estarán asociados con ninguna rama, lo que significa que podrías perderlos si cambias de rama sin guardarlos adecuadamente.

#### 5.1 Crear una nueva rama desde el commit actual:
````bash
git switch -c nueva-rama
````
Esto creará una nueva rama llamada "nueva-rama" y te moverá a esa rama, conservando todos los cambios que hiciste en el estado de "cabeza desprendida".

#### 5.2 Volver a una rama existente:
Si prefieres volver a una rama existente en lugar de crear una nueva, puedes cambiar a esa rama utilizando el comando: `git switch nombre-de-la-rama`.
Por ejemplo:
````bash
git switch main
````
Esto te llevará de vuelta a la rama principal (o a la rama que especifiques) y te permitirá trabajar desde allí.

#### 5.3 Descartar cambios y volver a la rama principal:
Si no quieres conservar los cambios que hiciste en el estado de "detached HEAD", puedes simplemente volver a la rama principal (o a la rama que estabas utilizando antes) con:
````bash
git switch -
````
Esto te llevará de vuelta a la rama en la que estabas antes de cambiar al estado de "cabeza desprendida", descartando cualquier cambio que hayas realizado en ese estado.


