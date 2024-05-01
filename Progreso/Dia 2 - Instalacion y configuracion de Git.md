# Instalación y Configuración de Git

## Instalación:

1. **Descarga Git:**
   - Visita [git-scm.com](https://git-scm.com/) y descarga la versión adecuada de Git para tu sistema operativo.

2. **Instalación en Windows:**
   - Ejecuta el archivo descargado y sigue las instrucciones del instalador. Asegúrate de seleccionar todas las opciones por defecto a menos que tengas una razón específica para cambiarlas.

3. **Instalación en macOS:**
   - Utiliza Homebrew para instalar Git ejecutando el siguiente comando en la terminal:
     ```bash
     brew install git
     ```

4. **Instalación en Linux (Ubuntu/Debian):**
   - Ejecuta el siguiente comando en la terminal:
     ```bash
     sudo apt-get install git
     ```

# Configuración Inicial:

5. **Configuración Global:**
   - Abre una terminal y configura tu nombre de usuario y tu dirección de correo electrónico utilizando los siguientes comandos:
     ```bash
     git config --global user.name "Tu Nombre"
     git config --global user.email "tu@email.com"
     ```

6. **Verificación de la Configuración:**
   - Puedes verificar la configuración global utilizando el siguiente comando:
     ```bash
     git config --global -e
     ```

7. **Editor de Texto por Defecto:**
   - Si quieres cambiar el editor de texto por defecto (que es visual studio code) utilizado por Git, puedes configurarlo con el siguiente comando:
     ```bash
     git config --global core.editor "nombre_del_editor"
     ```
   - Por ejemplo, para usar Sublime Text:
     ```bash
     git config --global core.editor "subl -n -w"
     ```

8. **Opciones de Configuración Adicionales:**
   - Git ofrece muchas opciones de configuración adicionales que puedes explorar en la [documentación oficial de Git](https://git-scm.com/docs/git-config).

## Verificación de la Instalación:

9. **Verificar la Instalación:**
   - Después de instalar Git, verifica que se haya instalado correctamente ejecutando el siguiente comando en la terminal:
     ```bash
     git --version
     ```
