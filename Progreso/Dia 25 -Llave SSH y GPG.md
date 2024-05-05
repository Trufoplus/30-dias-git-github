# LLave SHH

SSH (Secure Shell) es un protocolo que te permite conectarte y autenticarte de forma segura con servicios y servidores remotos. Al usar claves SSH, puedes acceder a repositorios en GitHub sin la necesidad de proporcionar tu nombre de usuario y token de acceso personal cada vez que visitas el sitio. Esto hace que la autenticación sea más segura y conveniente.

Para configurar SSH, primero necesitas generar una nueva clave SSH privada y agregarla al agente SSH en tu sistema. Luego, debes agregar la clave SSH pública a tu cuenta de GitHub para poder autenticarte y firmar confirmaciones de forma segura.

Para garantizar una seguridad adicional, puedes utilizar una llave de seguridad de hardware o agregar una contraseña a tu llave SSH. Además, es importante revisar regularmente tu lista de llaves SSH y eliminar aquellas que sean inválidas o que representen un riesgo de seguridad.

GitHub también elimina automáticamente las claves SSH inactivas después de un año como medida de seguridad adicional. Además, en organizaciones que utilizan GitHub Enterprise Cloud, se pueden proporcionar certificados SSH para acceder a repositorios sin necesidad de agregar el certificado a la cuenta de GitHub.

# Cómo crear una llave SSH y conectar a repositorios remotos

1. **Genera tu llave SSH:**
   - Abre tu terminal y ejecuta el siguiente comando (no es necesario ir a la carpeta de tu proyecto):
     ```bash
     ssh-keygen -t rsa -b 4096 -C "tu_email@example.com"
     ```
   - Presiona "Enter" y te saldra para aceptar la ubicación predeterminada del archivo de llave, dale "Enter" para aceptar o introduce la ubicacion donde quieras que se guarda la key.
   ```bash
    Enter file in which to save the key (/c/Users/dani_/.ssh/id_rsa):
   ```
   - Si deseas, puedes agregar una contraseña para tu llave SSH para mayor seguridad o dale a enter y dejala vacia, te lo pedira otra vez para confirmar.

2. **Agrega tu llave SSH a tu agente SSH:**
   - Si usas un agente SSH, añade tu llave SSH ejecutando el siguiente comando:
     ```bash
     ssh-add ~/.ssh/id_rsa
     ```

3. **Agrega tu llave SSH a tu cuenta de GitHub:**
   - Copia tu clave pública ejecutando:
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - Ve a tu cuenta de GitHub, haz clic en tu avatar en la esquina superior derecha y selecciona "Settings".
   - En el menú de la izquierda, haz clic en "SSH and GPG keys".
   - Haz clic en "New SSH key", pega tu clave pública y dale un nombre descriptivo.
   - Haz clic en "Add SSH key".

4. **Usa tu llave SSH para acceder a repositorios remotos:**
   - Ahora puedes clonar repositorios utilizando el protocolo SSH en lugar de HTTPS.

   - Para clonar un repositorio, usa el URL SSH proporcionado por el repositorio y ejecuta el comando `git clone` seguido del URL.

    ![ssh-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/ssh-1.png)

5. **Gestión de llaves SSH:**
   - Si necesitas eliminar o cambiar tu llave SSH, puedes hacerlo eliminando el archivo correspondiente en el directorio `~/.ssh/`.
   - Si alguna vez necesitas eliminar todas tus llaves SSH, ejecuta:
     ```bash
     rm -rf ~/.ssh
     ```

Una vez configurada, tu llave SSH te permitirá autenticarte de forma segura en repositorios remotos sin tener que ingresar tu nombre de usuario y contraseña cada vez.
