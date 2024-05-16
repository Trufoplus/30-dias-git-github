## CONFIGURACION
- ``git config --global user.name [nombre-usuario]`` Establece tu nombre de usuario
- ``git config --global user.email [email]`` Establece tu direccion de email
- ``git config --global -e`` Fichero con la informacion de configuracion git(nombre usuario, email, shortcuts, etc..)
- ``git remote ser -url origin [Nueva URL]`` Cambiar la url del repositorio remoto
  
## RAMAS (BRANCHES)
- ``git branch`` Muestra las ramas creadas en nuestro repositorio
- ``git branch [nombre-rama]`` --> Crear una rama
   - Nombre de las ramas en kebab case.  Ej: 'mi-rama-dev'
- ``git swicht [rama]`` --> Para movernos entre ramas (Creada para movernos entre rama)
- ``git checkout [rama]`` --> Para movernos entre ramas (version antigua, usar para archivos)
- ``git checkout -b [rama-nueva]`` --> Crea la rama y nos movemos a la nueva rama
- ``git switch -c [rama-nueva]`` --> Crea la rama y nos movemos a esa nueva rama
- ``git branch -d [nombre-rama]`` --> Borra la rama seleccionada
- ``git branch -m [rama] [nuevo nombre]`` --> Cambiar el nombre de una rama
- ``git branch -m [nuevo nombre]`` --> Cambiar el nombre de la rama en la que estamos ubicado

## FUSIONAR RAMAS (MERGE)
- ``git merge [nombre rama]`` Fusiona el contenido de la rama seleccionada a la rama en la que estamos colocados.
- ``git reset --hard [hash commit]`` Deshacer el merge, deshaciendo el commit fusionado en el merge anterior.
- ``git log --online -all`` Muestra los commit realizados en todas las ramas creadas


