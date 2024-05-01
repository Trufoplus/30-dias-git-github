# Alternativas a git log y git status

## `git log --oneline --decorate --all --graph`:

- **`git log`**: Muestra el historial de commits en el repositorio.
- **`--oneline`**: Muestra cada commit en una sola línea, lo que hace que la salida sea más compacta y fácil de leer.
- **`--decorate`**: Muestra las referencias de ramas y etiquetas junto a los commits en el historial.
- **`--all`**: Muestra todos los commits de todas las ramas, no solo la rama actual.
- **`--graph`**: Muestra una representación gráfica del historial de commits, mostrando las bifurcaciones y fusiones de las ramas.

Este comando es útil para obtener una vista general rápida y visual del historial de commits y las relaciones entre las ramas en un repositorio Git.

## `git status -s -b`:

- **`git status`**: Muestra el estado actual del repositorio, incluyendo los cambios sin hacer commit y el estado de las ramas.
- **`-s`**: Muestra un resumen corto y conciso del estado del repositorio, mostrando solo los nombres de los archivos con cambios.
- **`-b`**: Muestra la rama actual en la que te encuentras trabajando.

Este comando es útil para verificar rápidamente el estado de tu repositorio, incluyendo los cambios pendientes de commit y la rama en la que estás trabajando actualmente. La opción `-s` hace que la salida sea más concisa, y la opción `-b` añade información sobre la rama actual.


# Para crear atajos para los comandos

### Paso 1: Abrir el Archivo de Configuración Global de Git

Abre tu terminal y ejecuta el siguiente comando para abrir el archivo de configuración global de Git en tu editor de texto predeterminado:

```bash
git config --global --e
```

### Paso 2: Crear los Atajos

Dentro del archivo de configuración, agrega los siguientes alias para los atajos deseados:

```bash
[alias]
    l = log --oneline --decorate --all --graph
    s = status -s -b
```

### Paso 3: Guardar y Salir del Editor

Guarda los cambios en el archivo de configuración y cierra el editor de texto.

### Paso 4: Verificar los Nuevos Atajos

Para asegurarte de que los atajos se hayan creado correctamente, puedes ejecutar los siguientes comandos en la terminal:

```bash
git l
```

Este comando debería ejecutar el equivalente a `git log --oneline --decorate --all --graph`.

```bash
git s
```

Este comando debería ejecutar el equivalente a `git status -s -b`.
