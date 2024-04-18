# QUE ES REBASE
Imagina que estás trabajando en tu propio proyecto, pero ves que otros han hecho cambios importantes en el proyecto principal (main). Quieres agregar esos cambios a tu trabajo sin perder lo que ya has hecho.

El comando `git rebase [rama]` te permite hacer eso. Mueve tus cambios a un lugar temporal, luego aplica los cambios del proyecto principal a tu trabajo. Así, tus cambios se basan en los últimos del proyecto principal, manteniendo todo ordenado y actualizado. Es como si reorganizaras tu trabajo para que esté al día con lo que otros están haciendo.

**Ejemplo:**
Imagina que estás trabajando en un proyecto de software con otros desarrolladores. Tienes tu propia rama llamada "*mi_feature*" donde estás trabajando en una nueva función para el proyecto. Mientras tanto, otros desarrolladores han estado haciendo cambios en la rama principal del proyecto, llamada "main".

1. En tu rama "mi_feature", has hecho dos commits:
    + Commit 1: Agregaste una funcionalidad básica.
    + Commit 2: Hiciste algunas mejoras adicionales.
2. En la rama principal "main", otro desarrollador ha hecho un nuevo commit:
    + Commit 3: Agregó una importante corrección de errores.

Ahora, quieres traer esa corrección de errores (Commit 3 de "main") a tu rama "mi_feature" sin perder tu propio progreso. Aquí es donde usarías el comando:
````bash
git rebase main
````
Para mover tus cambios a un lugar temporal.
Luego, se aplicaría los cambios de la rama principal a tu rama "mi_feature".
Como resultado, tu rama "mi_feature" estaría actualizada con la corrección de errores de la rama principal, manteniendo tus propios cambios intactos.
.


# REBASE INTERACTIVO


El rebase interactivo es una característica avanzada de Git que te permite modificar los commits de una rama de manera más flexible y controlada.

Imagina que estás trabajando en tu propia rama con varios commits. Con el "rebase interactivo", puedes reorganizar y ajustar estos commits antes de integrarlos con otra rama tales como:

1. **Reorganización**: Puedes ordenar tus commits en el orden que desees, incluso cambiar sus mensajes y descripciones.
2. **Edición**: Puedes mejorar, editar o cambiar los mensajes y descripciones de tus commits. Esto es útil si algunos mensajes no están claros o necesitan ajustes.
3. **Unión y Separación de Commits**: Puedes combinar varios commits en uno solo si tienen cambios relacionados. Por otro lado, también puedes dividir un commit en varios si contiene demasiados cambios o funcionalidades distintas.


# Combinar dos commits en uno solo con REBASE INTERACTIVO


1. **Uso del "rebase interactivo" para combinar commits:** Se utiliza el comando `git rebase -i HEAD~2` para iniciar el rebase interactivo y combinar los dos últimos commits. Esto abrirá una ventana de edición donde se pueden combinar los commits.

2. **Selección de los commits a combinar:** Se te abrira una venta de vscode de edición, en dicha ventana, cambia la palabra "pick", por "squash" para el segundo commit, indicando que se quiere combinar con el commit anterior. El primer commit se deja como está. y cierras la ventana.

![unir dos commits](https://about.gitlab.com/images/blogimages/how-to-keep-your-git-history-clean-with-interactive-rebase/squash-mark-commit@2x.png)

3. **Edición del mensaje del commit combinado:** se te volvera a abrir otra ventana, Se edita el mensaje del commit combinado en la ventana de edición.

4. **Finalización del rebase interactivo:** Se guarda y se cierra la ventana de edición. El rebase interactivo se completa exitosamente y los commits se combinan en uno solo.

5. **Verificación de los cambios:** Se verifica que los cambios se han combinado correctamente con ``git log`` y que el archivo "Redmi" no ha sido afectado de manera inesperada.

# COMANDO DE LA VENTANA REBASE INTERACTIVO

Aquí tienes una explicación de los comandos que se pueden utilizar con el rebase interactivo y su significado:

- **pick (recoger):** Este comando se usa para mantener el commit tal como está. No se realiza ninguna acción sobre él durante el rebase interactivo.

- **squash (aplastar):** Se utiliza para fusionar un commit con el commit anterior, combinando sus cambios en uno solo. Se debe proporcionar un nuevo mensaje para el commit resultante que incluya los cambios de ambos commits.

- **fixup (arreglar):** Similar a squash, este comando fusiona un commit con el commit anterior, pero descarta su mensaje de commit. Se utiliza cuando no se necesita conservar el mensaje del commit que se está fusionando.

- **edit (editar):** Permite editar el mensaje de un commit durante el rebase interactivo. Se puede utilizar para modificar el mensaje del commit o para realizar cambios adicionales en los archivos del commit.

- **reword (reescribir):** Similar a edit, pero se utiliza principalmente para cambiar el mensaje del commit sin realizar cambios adicionales en los archivos del commit.

- **drop (eliminar):** Se utiliza para eliminar un commit durante el rebase interactivo. El commit y sus cambios se eliminan del historial de commits.

- **exec (ejecutar):** Permite ejecutar un comando shell durante el rebase interactivo. Se utiliza para realizar acciones personalizadas durante el proceso de rebase.



