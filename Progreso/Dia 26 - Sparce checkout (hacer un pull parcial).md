# Sparse Checkout

La función `sparse checkout` en Git permite a los usuarios configurar un repositorio para que solo tenga en el espacio de trabajo una parte específica de los directorios del repositorio. Esto puede ser útil cuando solo estás interesado en trabajar con una parte específica del proyecto y no necesitas descargar o mantener el historial completo del repositorio.

## Paso a paso

### 1. Configurar sparse checkout:

Antes de usar sparse checkout, debes activarlo en tu repositorio con el siguiente comando:

```bash
git config core.sparseCheckout true
```

### 2. Abrir el archivo sparse-checkout 

Abre el archivo `.git/info/sparse-checkout` en tu repositorio. En este archivo, puedes especificar los archivos y directorios que deseas incluir en tu espacio de trabajo:

```bash
code .git/info/sparse-checkout
```

Puedes utilizar tu editor preferido, como Vim, Nano, etc.

### 3. Definir los patrones de archivos/directorios

Cada línea del archivo representa un patrón de inclusión o exclusión utilizando el formato de patrón de Git.

- **Patrones de inclusión:** Son archivos o directorios que deseas incluir en tu espacio de trabajo.
  - `carpeta/` -> incluirá la carpeta y todo su contenido
  - `*.txt` -> incluirá todos los archivos .txt
  - `carpeta/*.md` incluirá todos los archivos con extensión .md dentro de la carpeta.

- **Patrones de exclusión:** Son archivos o directorios que deseas excluir de tu espacio de trabajo. Simplemente agrega `!` delante del tipo de archivo. Los archivos de exclusión tienen prioridad sobre los archivos de inclusión. Algunos ejemplos:
  - `!carpeta/` excluye la carpeta.
  - `!*.py` excluye todos los archivos .py

Ejemplo:

```bash
img/
scripts/*.py
!README.md
```

### 4. Actualizar el índice:

Después de definir los patrones de inclusión/exclusión en el archivo `.git/info/sparse-checkout`, usa el siguiente comando para que solo se reflejen los archivos y directorios especificados:

```bash
git read-tree -mu HEAD
```

## Desactivar y eliminar el sparse checkout

1. **Desactivar el sparse checkout:**
   
   Para desactivar el sparse checkout, simplemente cambia la configuración `core.sparseCheckout` a `false`. Puedes hacerlo ejecutando el siguiente comando en tu repositorio:

   ```bash
   git config core.sparseCheckout false
   ```

2. **Eliminar el archivo `.git/info/sparse-checkout`:**

   El archivo `.git/info/sparse-checkout` es donde se almacenan los patrones de inclusión y exclusión cuando se usa `sparse checkout`. Puedes eliminar este archivo ejecutando el siguiente comando:

   ```bash
   rm .git/info/sparse-checkout
   ```

3. **Restaurar el espacio de trabajo:**
   
   Si usas `ls`, es posible que no aparezcan todos los archivos de tu directorio. Para restaurar el espacio de trabajo después de eliminar el sparse checkout, puedes utilizar el comando `git sparse-checkout disable`. Este comando deshabilitará la configuración `core.sparseCheckout` y restaurará el espacio de trabajo para incluir todos los archivos:

   ```bash
   git sparse-checkout disable
   ```




