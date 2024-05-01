# Vim

Vim es un editor de texto muy potente y altamente configurable que se ejecuta en la línea de comandos. Es muy utilizado por programadores y administradores de sistemas debido a su eficiencia y capacidad para manejar grandes archivos de texto. Aquí tienes una breve introducción al uso de Vim y algunos comandos básicos:

# Uso Básico de Vim:

1. **Abrir un Archivo con Vim:**
    - Primero abrimos la terminal creamos un archivo con los comando ``touch archivo.txt``, luego podemos verificar que esta creado con el comando ``ls``.

    - Luego abrimos en vim para su edicion con el comando:

   ```bash
   vim nombre_del_archivo
   ```

   - Podemos autocompletar el nombre del archivo solo escribiendo la primera letra y dandole a la tecla "TAB" del teclado autocompletara el nombre.

2. **Modo de Inserción (Insert Mode):**
   - Presiona la tecla `i` para entrar en el modo de inserción. En este modo, puedes escribir y editar el texto como lo harías en un editor de texto normal.

3. **Modo de Comandos (Command Mode):**
   - Presiona la tecla `Esc` para salir del modo de inserción y entrar en el modo de comandos. Desde aquí, puedes ejecutar comandos de Vim.

4. **Guardar y Salir:**
   - En el modo de comandos, puedes guardar los cambios y salir de Vim con el comando `:wq` y luego presionar `Enter`.
   - Para salir sin guardar cambios, puedes usar `:q!`.
   - Para alir si no has hecho ningun cambio ``:q``
   - puedes leer el archivo con el comando ``cat archivo.txt`` y eliminarlo con ``rm archivo.tct``

5. **Moverse por el Texto:**
   - Utiliza las teclas de flecha para moverte por el texto.
   - Usa las teclas `h`, `j`, `k` y `l` para moverte hacia la izquierda, abajo, arriba y derecha respectivamente.

6. **Borrar, Copiar y Pegar:**
   - En el modo de comandos, puedes borrar texto con comandos como `x` para borrar un carácter, `dd` para borrar una línea entera, etc.
   - Para copiar y pegar, puedes usar comandos como `yy` para copiar una línea, `p` para pegar, etc.

7. **Buscar y Reemplazar:**
   - En el modo de comandos, puedes buscar texto con el comando `/texto_a_buscar`.
   - Para reemplazar texto, usa el comando `:%s/texto_a_buscar/texto_nuevo/g` para reemplazar todas las ocurrencias en el archivo.

8. **Cheat Sheet:**

![](https://github.com/Trufoplus/30-dias-git-github/blob/main/Recursos/Comandos%20Vim.jpg)

