# Pull Requests

Un pull request es como pedir permiso para incluir cambios en un proyecto de programación. Imagina que eres el usuario A en una empresa y tienes algunas ideas nuevas para mejorar el código. Pero, no puedes simplemente agregar tus cambios directamente a la versión principal que los clientes usan. Antes, necesitas solicitar una revisión.

Entonces, haces un pull request, que es básicamente una solicitud de revisión para tus cambios. EL equipo revisa tus cambios y decide si están listos para ser fusionados con la versión principal del código. Pueden decir "sí, adelante" y fusionar tus cambios, o pueden sugerir mejoras antes de aceptarlos.

El pull request es importante porque ayuda a controlar el proceso de desarrollo. Asegura que los cambios sean revisados antes de ser incluidos en la versión final del código que usan los clientes. Esto ayuda a prevenir errores y garantiza que todos estén de acuerdo con los cambios antes de que se apliquen. Es una forma de mantener el código limpio y seguro para todos los usuarios.

# Como hacer un PR (pull requests).
Vamos a crear un pull requests en nuestro proyecto.

1. **Crear una nueva rama:** Primero, creamos una nueva rama que he llamado "Rama-pull-requests" utilizando el comando `git branch [nombre_rama]`.
   
2. **Cambiar a la nueva rama:** Luego, cambiamos a la nueva rama utilizando el comando `git checkout`.

3. **Realizar cambios:** Trabajamos en la nueva rama haciendo las modificaciones deseadas en los archivos del proyecto. En este caso, se modifica un archivo llamado "Historia.md".

4. **Agregar y confirmar cambios:** Agregamos y confirmamos los cambios realizados utilizando los comandos `git add` y `git commit`.

5. **Enviar cambios al repositorio remoto:** Luego, enviamos los cambios de la nueva rama al repositorio remoto utilizando el comando `git push`.

6. **Crear un pull request:** Una vez que los cambios están en el repositorio remoto, creamos un pull request desde la plataforma de GitHub. Una vez entremos no s aparecera un mensaje indicado que una de la ramas secundarias del proyecto ha recibido recientemente un push, selecciona en compare & pull requests.

![pull-requests-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/pull-requests-1.png)

7. **Describir el pull request:** Es importante proporcionar una descripción clara y concisa del pull request, explicando los cambios realizados y su propósito.

![pull-requests-2](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/pull-requests-2.png)

8. **Revisión del pull request:** Los colaboradores del proyecto revisarán el pull request y podrán dejar comentarios, sugerencias o aprobar los cambios para fusionar o no los cambios en la rama secundaria con la rama principal.

9. **Realizar el merge:** Si los cambios son aprobados, se realiza el merge del pull request, lo que significa que los cambios se incorporan a la rama objetivo del proyecto.

![pull-requests-4](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/pull-requests-4.png)

10. **Eliminar la rama:** Una vez que el pull request se ha fusionado con éxito, podemos eliminar la rama utilizada para el pull request tanto en el repositorio local como en el remoto.

### Buenas prácticas en GitHub y Git

Cuando trabajamos con Git y GitHub, es crucial seguir ciertas buenas prácticas para mantener un flujo de trabajo ordenado y evitar problemas. Estas prácticas son aplicables tanto en entornos empresariales como en proyectos personales. A continuación, destacaremos algunas de estas prácticas:

1. **Ramas principales:** Es esencial tener claras las ramas principales, como la rama "master" o "main". Estas ramas deben ser tratadas con cuidado, ya que representan la versión final del proyecto. Cualquier conflicto en estas ramas puede ser problemático y debe resolverse rápidamente.

2. **Creación de ramas secundarias:** Para desarrollar nuevas funcionalidades o implementar cambios, es recomendable crear ramas secundarias apartadas de la rama principal. Estas ramas secundarias pueden ser utilizadas por diferentes desarrolladores para trabajar en diferentes funcionalidades simultáneamente.

3. **Implementación progresiva:** En cada rama secundaria, se debe trabajar progresivamente hacia el objetivo establecido. Por ejemplo, si una rama se crea para implementar una nueva funcionalidad, se deben realizar y confirmar los cambios relacionados con esa funcionalidad antes de proponer un pull request.

4. **Solicitar revisión:** Antes de fusionar una rama secundaria con la rama principal, es importante solicitar una revisión por parte de otros colaboradores del proyecto por medio de un pull requests de tu rama secundaria a la rama principal. Esta revisión garantiza la calidad del código y ayuda a identificar posibles problemas antes de la fusión.

5. **Fusionar con la rama principal:** Una vez que los cambios en una rama secundaria han sido revisados y aprobados, se puede proceder a fusionar la rama con la rama principal. Es fundamental asegurarse de que no haya conflictos y de que los cambios se integren correctamente en la rama principal.

6. **Eliminar ramas secundarias:** Después de fusionar una rama secundaria con éxito, es recomendable eliminar la rama secundaria para mantener un repositorio limpio y organizado.

7. **Utilizar herramientas de GitHub:** GitHub proporciona herramientas útiles, como pull requests, para facilitar la revisión y la colaboración en proyectos. Es importante familiarizarse con estas herramientas y utilizarlas de manera efectiva para gestionar el flujo de trabajo del proyecto.

Siguiendo estas buenas prácticas, podemos trabajar de manera eficiente y colaborativa en proyectos de desarrollo de software, evitando problemas y manteniendo la calidad del código en todo momento.




