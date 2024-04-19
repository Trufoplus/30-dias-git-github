# Repositorio Local vs Repositorio Remoto
 1. **Repositorio Local:**
    + Un repositorio local es una copia del proyecto de software que resides en tu propia computadora.
    + Contiene todos los archivos y el historial de cambios del proyecto.
    + Los cambios en el código se guardan y gestionan localmente, lo que significa que solo tú tienes acceso y control sobre ellos.
    + Permite a los desarrolladores trabajar en su código sin necesidad de una conexión a Internet.
    + Los cambios en el código se pueden realizar, deshacer y revisar localmente antes de ser compartidos con otros colaboradores.

![](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/local_vs_remoto.png)

2. **Repositorio Remoto:**
    + Un repositorio remoto es una copia del proyecto que se encuentra en un servidor remoto, como GitHub, GitLab o Bitbucket.
    + Permite a varios desarrolladores trabajar en el mismo proyecto de manera colaborativa desde diferentes ubicaciones geográficas.
    + Todos los colaboradores tienen acceso al mismo código y pueden ver los cambios realizados por otros.
    + Facilita la colaboración y el trabajo en equipo al proporcionar un punto centralizado para almacenar y gestionar el código.
    + Los cambios en el código se pueden enviar desde el repositorio local al remoto (push) para que otros puedan verlos, y también se pueden descargar desde el repositorio remoto al local (pull) para mantenerse actualizado con los cambios realizados por otros colaboradores.


# ¿Qué es GitHub?
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxXFgLqvujcAvXFxmkBW3Y1U16pC6UAYA3xw&s)

GitHub es una plataforma de desarrollo colaborativo para alojar proyectos utilizando el sistema de control de versiones Git. Es ampliamente utilizada por desarrolladores de software para trabajar en equipo, coordinar proyectos y realizar un seguimiento de las modificaciones realizadas en el código fuente. En GitHub, los usuarios pueden alojar repositorios de código, contribuir a proyectos existentes, colaborar con otros desarrolladores, y también realizar un seguimiento de problemas y solicitudes de incorporación de cambios (pull requests). Además, ofrece herramientas para la gestión de proyectos, seguimiento de problemas, integración continua y despliegue automatizado, entre otras funcionalidades.

## Repositorios de GitHub



Los repositorios en GitHub son espacios donde se almacena y gestiona el código de un proyecto. Estos repositorios pueden contener todo tipo de archivos relacionados con el desarrollo de software, como código fuente, documentación, imágenes, archivos de configuración, entre otros.

1. **Creación de repositorios:** Los usuarios pueden crear repositorios nuevos en GitHub con tan solo unos pocos clics. Pueden optar por hacerlos públicos (accesibles para todos) o privados (accesibles solo para los colaboradores designados).

2. **Clonación de repositorios:** Los desarrolladores pueden clonar (copiar) repositorios de GitHub en sus máquinas locales para trabajar en ellos. Esto les permite realizar cambios en el código y luego subir esos cambios de vuelta al repositorio en línea.

3. **Seguimiento de versiones:** GitHub utiliza Git como su sistema de control de versiones, lo que significa que cada cambio realizado en un repositorio se registra y puede revertirse si es necesario. Esto facilita el seguimiento de los cambios realizados en el código a lo largo del tiempo.

4. **Colaboración:** Los repositorios de GitHub son lugares donde los equipos pueden colaborar en proyectos de software. Varios desarrolladores pueden trabajar juntos en un repositorio, proponer cambios (mediante "solicitudes de incorporación de cambios" o "pull requests") y revisar el código de los demás.

5. **Gestión de problemas y solicitudes de incorporación de cambios:** Los repositorios de GitHub incluyen herramientas para realizar un seguimiento de problemas (bugs, mejoras, tareas pendientes, etc.) y para gestionar las solicitudes de incorporación de cambios. Esto facilita la comunicación entre los miembros del equipo y el seguimiento del progreso del proyecto.


# COMANDOS BASICOS DE GITHUB

+ `git remote add origin <URL>`: Este comando se utiliza para agregar un repositorio remoto a tu repositorio local. El término **origin** es un nombre convencional para el repositorio remoto principal, pero puede ser cualquier otro nombre. La **URL** es la dirección del repositorio remoto al que deseas conectar tu repositorio local.

+ `git remote`: Este comando te muestra los repositorios remotos que están configurados actualmente en tu repositorio local. En este caso, al tener solo uno 
configurado (llamado `origin`), solo se muestra ese. Pero si has hecho un fork del repositortio de _KontrolDev_ entonces te aparecera tambien `upstream` que seria el repositorio original del que has hecho un fork. Se suele utilizar comúnmente para mantenerse sincronizado con el repositorio original del proyecto.

````bash
$ git remote
origin
upstream
````

+ ``git remote -v``: Este comando muestra los detalles de los repositorios remotos configurados, incluyendo la URL. El -v indica que se desea una salida más detallada.
````bash
$ git remote -v
origin  https://github.com/oniricoh/30-dias-git-github.git (fetch)
origin  https://github.com/oniricoh/30-dias-git-github.git (push)
upstream        https://github.com/kontroldev/30-dias-git-github.git (fetch)
upstream        https://github.com/kontroldev/30-dias-git-github.git (push)
````

+ ``git fetch``: Este comando descarga cambios desde el repositorio remoto a tu repositorio local, pero no los fusiona automáticamente con tu trabajo actual. Es útil para obtener una vista previa de los cambios antes de fusionarlos.

+ ``git push -u origin <nombre-de-la-rama>``: Este comando se utiliza para enviar tus cambios locales al repositorio remoto. El -u es para configurar la rama remota como la rama upstream, lo que significa que en futuros git push no necesitarás especificar la rama y se enviarán automáticamente a esa rama remota. <nombre-de-la-rama> es el nombre de la rama que estás enviando al repositorio remoto.

````bash
$ git push -u origin main
#Resultado:
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 18.49 KiB | 9.25 MiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: This repository moved. Please use the new location:
remote:   https://github.com/Trufoplus/30-dias-git-github.git
To https://github.com/oniricoh/30-dias-git-github.git
   f678672..ffc1f65  main -> main
branch 'main' set up to track 'origin/main'.
````
